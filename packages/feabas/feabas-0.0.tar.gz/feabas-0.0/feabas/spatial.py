from collections import defaultdict, OrderedDict

import cv2
import h5py
import numpy as np
import shapely.geometry as shpgeo
from shapely.ops import unary_union, linemerge
from shapely import wkb

from feabas import dal, miscs, material


JOIN_STYLE = shpgeo.JOIN_STYLE.mitre


def fit_affine(pts0, pts1, return_rigid=False):
    # pts0 = pts1 @ A
    pts0 = pts0.reshape(-1,2)
    pts1 = pts1.reshape(-1,2)
    assert pts0.shape[0] == pts1.shape[0]
    mm0 = pts0.mean(axis=0)
    mm1 = pts1.mean(axis=0)
    pts0 = pts0 - mm0
    pts1 = pts1 - mm1
    pts0_pad = np.insert(pts0, 2, 1, axis=-1)
    pts1_pad = np.insert(pts1, 2, 1, axis=-1)
    res = np.linalg.lstsq(pts1_pad, pts0_pad, rcond=None)
    r1 = np.linalg.matrix_rank(pts0_pad)
    A = res[0]
    r = min(res[2], r1)
    if r == 1:
        A = np.eye(3)
        A[-1,:2] = mm0 - mm1
    elif r == 2:
        pts0_rot90 = pts0[:,::-1] * np.array([1,-1])
        pts1_rot90 = pts1[:,::-1] * np.array([1,-1])
        pts0 = np.concatenate((pts0, pts0_rot90), axis=0)
        pts1 = np.concatenate((pts1, pts1_rot90), axis=0)
        pts0_pad = np.insert(pts0, 2, 1, axis=-1)
        pts1_pad = np.insert(pts1, 2, 1, axis=-1)
        res = np.linalg.lstsq(pts1_pad, pts0_pad, rcond=None)
        A = res[0]
    if return_rigid:
        u, _, vh = np.linalg.svd(A[:2,:2], compute_uv=True)
        R = A.copy()
        R[:2,:2] = u @ vh
        R[-1,:2] = R[-1,:2] + mm0 - mm1 @ R[:2,:2]
        R[:,-1] = np.array([0,0,1])
    A[-1,:2] = A[-1,:2] + mm0 - mm1 @ A[:2,:2]
    A[:,-1] = np.array([0,0,1])
    if return_rigid:
        return A, R
    else:
        return A



def scale_coordinates(coordinates, scale):
    """
    scale coordinates, at the same time align the center of the top-left corner
    pixel to (0, 0).
    """
    coordinates = np.array(coordinates, copy=False)
    if scale == 1:
        return coordinates
    else:
        return (coordinates + 0.5) * scale - 0.5



def find_contours(mask):
    """
    wrapper of findContour function in opencv to accommodate version change.
    """
    approx_mode = cv2.CHAIN_APPROX_SIMPLE  # cv2.CHAIN_APPROX_NONE
    if not np.any(mask):
        return (), None
    mask = mask.astype(np.uint8, copy=False)
    if cv2.__version__ < '4':
        _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, approx_mode)
    else:
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, approx_mode)
    return contours, hierarchy



def countours_to_polygon(contours, hierarchy, offset=(0,0), scale=1.0):
    """
    convert opencv contours to shapely (Multi)Polygons.
    Args:
        contours, hierarchy: output from find_countours.
    Kwargs:
        offsets: x, y translation offset to add to the output polygon.
        scale: scaling factor of the geometries.
    """
    polygons_staging = {}
    holes = {}
    buffer_r = 0.5 * scale # expand by half pixel
    for indx, ct in enumerate(contours):
        number_of_points = ct.shape[0]
        if number_of_points < 3:
            continue
        xy = scale_coordinates(ct.reshape(number_of_points, -1) + np.asarray(offset), scale=scale)
        lr = shpgeo.polygon.LinearRing(xy)
        pp = shpgeo.polygon.orient(shpgeo.Polygon(lr))
        if lr.is_ccw:
            holes[indx] = pp
        else:
            polygons_staging[indx] = pp
    if len(polygons_staging) == 0:
        return None     # no region found
    hierarchy = hierarchy.reshape(-1, 4)
    for indx, hole in holes.items():
        parent_indx = hierarchy[indx][3]
        if parent_indx not in polygons_staging:
            raise RuntimeError('found an orphan hole...') # should never happen
        polygons_staging[parent_indx] = polygons_staging[parent_indx].difference(hole)
    return unary_union(list(polygons_staging.values())).buffer(buffer_r, join_style=JOIN_STYLE)



def images_to_polygons(imgs, labels, offset=(0, 0), scale=1.0):
    """
    Convert images to shapely Polygons.
    Args:
        imgs(MosaicLoader/ndarray/str): label images.
        labels (OrderedDict): names to labels mapper.
    Kwargs:
        offsets: global x, y translation offset to add to the output polygons.
            the scaling of the offsets is the same as the images.
        scale: scaling factor of the geometries.
    """
    if not isinstance(labels, dict):
        labels = OrderedDict((str(s), s) for s in labels)
    polygons = {}
    if isinstance(imgs, dal.MosaicLoader):
        xmin, ymin, xmax, ymax = imgs.bounds
        # align bounds to corners of pixels by substracting 0.5
        xmin += offset[0] - 0.5
        xmax += offset[0] - 0.5
        ymin += offset[1] - 0.5
        ymax += offset[1] - 0.5
        xmin, ymin, xmax, ymax = scale_coordinates((xmin, ymin, xmax, ymax), scale)
        extent = shpgeo.box(xmin, ymin, xmax, ymax)
        regions_staging = defaultdict(list)
        for bbox in imgs.file_bboxes(margin=3):
            tile = imgs.crop(bbox, return_empty=False)
            if tile is None:
                continue
            xy0 = np.array(bbox[:2], copy=False) + np.array(offset)
            for name, lbl in labels.items():
                if lbl is None:
                    continue
                if len(tile.shape) > 2: # RGB
                    mask = np.all(tile == np.array(lbl), axis=-1)
                else:
                    mask = (tile == lbl)
                ct, h = find_contours(mask)
                pp = countours_to_polygon(ct, h, offset=xy0, scale=scale)
                if pp is not None:
                    regions_staging[name].append(pp)
        for name, pp in regions_staging.items():
            p_lbl = unary_union(pp)
            if p_lbl.area > 0:
                polygons[name] = p_lbl
    else:
        if isinstance(imgs, str): # input is a file path
            tile = cv2.imread(imgs, cv2.IMREAD_UNCHANGED)
        elif isinstance(imgs, np.ndarray):
            tile = imgs
        else:
            raise TypeError
        xmin = offset[0] - 0.5
        xmax = offset[0] + tile.shape[1] - 0.5
        ymin = offset[1] - 0.5
        ymax = offset[1] + tile.shape[1] - 0.5
        xmin, ymin, xmax, ymax = scale_coordinates((xmin, ymin, xmax, ymax), scale)
        extent = shpgeo.box(xmin, ymin, xmax, ymax)
        for name, lbl in labels.items():
            if lbl is None:
                continue
            if len(tile.shape) > 2: # RGB
                mask = np.all(tile == np.array(lbl), axis=-1)
            else:
                mask = (tile == lbl)
            ct, h = find_contours(mask)
            p_lbl = countours_to_polygon(ct, h, offset=np.array(offset), scale=scale)
            if p_lbl is not None:
                polygons[name] = p_lbl
    return polygons, extent



def get_polygon_representative_point(poly):
    """
    Get representative point(s) for shapely (Multi)Polygon.
    """
    if hasattr(poly, 'geoms'):
        points = []
        for elem in poly.geoms:
            pts = get_polygon_representative_point(elem)
            points.extend(pts)
    elif isinstance(poly, shpgeo.Polygon):
        points = list(poly.representative_point().coords)
    else:
        points = []
    return points



def polygon_area_filter(poly, area_thresh=0):
    if area_thresh == 0:
        return poly
    if isinstance(poly, shpgeo.Polygon):
        if shpgeo.Polygon(poly.exterior).area < area_thresh:
            return None
        Bs = poly.boundary
        if hasattr(Bs,'geoms'):
            # may need to fill small holes
            holes_to_fill = []
            for linestr in Bs.geoms:
                pp = shpgeo.Polygon(linestr)
                if pp.area < area_thresh:
                    holes_to_fill.append(pp)
            if len(holes_to_fill) > 0:
                return poly.union(unary_union(holes_to_fill))
            else:
                return poly
        else:
            return poly
    elif isinstance(poly, shpgeo.MultiPolygon):
        new_poly_list = []
        for pp in poly.geoms:
            pp_updated = polygon_area_filter(pp, area_thresh=area_thresh)
            if pp_updated is not None:
                new_poly_list.append(pp_updated)
        if len(new_poly_list) > 0:
            return unary_union(new_poly_list)
        else:
            return None
    elif isinstance(poly, dict):
        new_dict = {}
        for key, pp in poly.items():
            pp_updated = polygon_area_filter(pp, area_thresh=area_thresh)
            if pp_updated is not None:
                new_dict[key] = pp_updated
        return new_dict
    elif isinstance(poly, (tuple, list)):
        new_list = []
        for pp in poly:
            pp_updated = polygon_area_filter(pp, area_thresh=area_thresh)
            if pp_updated is not None:
                new_list.append(pp_updated)
        if isinstance(poly, tuple):
            new_list = tuple(new_list)
        return new_list
    else:
        raise TypeError




class Geometry:
    """
    Class to represent a collection of 2d geometries that defines the shapes of
    subregions within a section. On each subregion we can assign its own
    mechanical properties

    Kwargs:
        roi(shapely Polygon or MultiPolygon): polygon the defines the shape of
            the outline of the geometry.
        regions(dict): dictionary contains polygons defining the shape of
            subregions with mechanical properties different from default.
        zorder(list): list of keys in the regions dict. If overlaps exist
            between regions, regions later in the list will trump early ones
    """
    def __init__(self, roi=None, regions={}, **kwargs):
        self._roi = roi
        self._regions = regions
        self._resolution = kwargs.get('resolution', 4.0)
        self._zorder = kwargs.get('zorder', list(self._regions.keys()))
        self._region_names = kwargs.get('region_names', None)
        self._committed = False


    @classmethod
    def from_image_mosaic(cls, image_loader, label_list=[200], region_names=None, **kwargs):
        """
        Args:
            image_loader(femaligner.dal.MosaicLoader): image loader to load mask
                images in mosaic form. Can also be a single-tile image
        kwargs:
            resolution(float): resolution of the geometries. Different scalings
                align at the top-left corner pixel as (0, 0).
            oor_label(int): label assigned to out-of-roi region.
            label_list(list): list of region labels to extract from the images.
            region_names(OrderedDict): OrderedDict mapping region names to their
                corresponding labels.
            dilate(float): dilation radius to grow regions.
            scale(float): if image_loader is not a MosaicLoader, use this to
                define scaling factor.
        """
        resolution = kwargs.get('resolution', 4.0)
        oor_label = kwargs.get('oor_label', None)
        roi_erosion = kwargs.get('roi_erosion', 0.5)
        dilate = kwargs.get('dilate', 0.1)
        scale = kwargs.get('scale', 1.0)
        if region_names is None:
            region_names = OrderedDict((str(s),s) for s in label_list)
        if isinstance(image_loader, dal.MosaicLoader):
            scale = image_loader.resolution / resolution
        if oor_label is not None:
            region_names.update({'out_of_roi_label': oor_label})
        regions, roi = images_to_polygons(image_loader, region_names, scale=scale)
        if roi_erosion > 0:
            roi = roi.buffer(-roi_erosion, join_style=JOIN_STYLE)
        if oor_label is not None and 'out_of_roi_label' in regions:
            pp = regions.pop('out_of_roi_label')
            if roi_erosion > 0:
                pp = pp.buffer(roi_erosion, join_style=JOIN_STYLE)
            roi = roi.difference(pp)
        if dilate > 0:
            for lbl, pp in regions.items():
                regions[lbl] = pp.buffer(dilate, join_style=JOIN_STYLE)
        return cls(roi=roi, regions=regions, resolution=resolution, zorder=list(region_names.keys()))


    @classmethod
    def from_h5(cls, h5name):
        kwargs = {}
        regions = {}
        with h5py.File(h5name, 'r') as f:
            if 'resolution' in f:
                kwargs['resolution'] = f['resolution'][()]
            if 'zorder' in f:
                kwargs['zorder'] = miscs.numpy_to_str_ascii(f['zorder'][()]).split('\n')
            if 'roi' in f:
                roi = wkb.loads(bytes.fromhex(f['roi'][()].decode()))
            if 'regions' in f:
                for rname in f['regions']:
                    regions[rname] = wkb.loads(bytes.fromhex(f['regions/'+rname][()].decode()))
        return cls(roi=roi, regions=regions, **kwargs)


    def save_to_h5(self, h5name):
        with h5py.File(h5name, 'w') as f:
            _ = f.create_dataset('resolution', data=self._resolution)
            if bool(self._zorder):
                zorder_encoded = miscs.str_to_numpy_ascii('\n'.join(self._zorder))
                _ = f.create_dataset('zorder', data=zorder_encoded)
            if hasattr(self._roi, 'wkb_hex'):
                _ = f.create_dataset('roi', data=self._roi.wkb_hex)
            for name, pp in self._regions.items():
                if hasattr(pp, 'wkb_hex'):
                    keyname = 'regions/{}'.format(name)
                    _ = f.create_dataset(keyname, data=pp.wkb_hex)


    def add_regions(self, regions, mode='u', pos=None):
        """
        add regions to geometry.
        Args:
            regions(dict): contains regions in shapely.Polygon format
        Kwargs:
            mode: 'u'-union; 'r'-replace.
            pos: position to insert in _zorder. None for append.
        """
        for lbl, pp in regions.items():
            if (mode=='r') or (lbl not in self._regions):
                self._regions[lbl] = pp
            else:
                self._regions[lbl] = self._regions[lbl].union(pp)
            if lbl not in self._zorder:
                if pos is None:
                    self._zorder.append(lbl)
                else:
                    self._zorder.insert(pos, lbl)
        self._committed = False


    def add_regions_from_image(self, image, label_list=[200], region_names=None, **kwargs):
        resolution = kwargs.get('resolution', 4.0)
        dilate = kwargs.get('dilate', 0.1)
        scale = kwargs.get('scale', 1.0)
        mode = kwargs.get('mode', 'u')
        pos = kwargs.get('pos', None)
        if isinstance(image, dal.MosaicLoader):
            scale = image.resolution / resolution
        if region_names is None:
            region_names = OrderedDict((str(s),s) for s in label_list)
        regions, _ = images_to_polygons(image, region_names, scale=scale)
        if dilate > 0:
            for lbl, pp in regions.items():
                regions[lbl] = pp.buffer(dilate, join_style=JOIN_STYLE)
        self.add_regions(regions, mode=mode, pos=pos)


    def modify_roi(self, roi, mode='r'):
        """
        modify the roi geometry.
        Args:
            roi(shapely Polygon)
        Kwargs:
            mode: 'u'-union; 'r'-replace; 'i'-intersect
        """
        if (mode == 'r') or self._roi is None:
            self._roi = roi
        elif mode == 'i':
            self._roi = self._roi.intersection(roi)
        else:
            self._roi = self._roi.union(roi)
        self._committed = False


    def modify_roi_from_image(self, image, roi_label=0, **kwargs):
        resolution = kwargs.get('resolution', 4.0)
        roi_erosion = kwargs.get('roi_erosion', 0)
        scale = kwargs.get('scale', 1.0)
        mode = kwargs.get('mode', 'r')
        if isinstance(image, dal.MosaicLoader):
            scale = image.resolution / resolution
        poly, extent = images_to_polygons(image, {'roi': roi_label}, scale=scale)
        if 'roi' in poly and poly['roi'].area > 0:
            roi = poly['roi']
        else:
            roi = extent
        if roi_erosion > 0:
            roi = roi.buffer(-roi_erosion, join_style=JOIN_STYLE)
        self.modify_roi(roi, mode=mode)


    def commit(self, **kwargs):
        """
        rectify the regions to make them mutually exclusive and within ROI.
        Kwargs:
            area_threshold(float): area threshold below which the regions should
                be discarded.
        """
        area_thresh = kwargs.get('area_thresh', 0)
        if self._roi is None:
            raise RuntimeError('ROI not defined')
        mask = self._roi
        covered_list = [mask]
        for lbl in reversed(self._zorder):
            if lbl not in self._regions:
                continue
            poly = (self._regions[lbl]).intersection(mask)
            poly_updated = polygon_area_filter(poly, area_thresh=area_thresh)
            if poly_updated is None:
                self._regions.pop(lbl)
            else:
                self._regions[lbl] = poly_updated
                covered_list.append(poly_updated)
                mask = mask.difference(poly_updated)
        filtered_roi = polygon_area_filter(mask, area_thresh=area_thresh)
        if filtered_roi is not None:
            self._roi = filtered_roi
        covered = unary_union(covered_list)
        covered_boundary = covered.boundary
        if hasattr(covered_boundary, 'geoms'):
            # if boundary has multiple line strings, check for holes
            holes_list = []
            max_area = 0
            outer_boundary = 0
            for linestr in covered_boundary.geoms:
                pp = shpgeo.Polygon(linestr)
                if pp.area < area_thresh:
                    # if smaller than the area threshold, fill with default material
                    self._roi = self._roi.union(pp)
                else:
                    holes_list.append(pp)
                    if pp.area > max_area: # largest area is the outer boundary
                        outer_boundary = len(holes_list) - 1
            holes_list.pop(outer_boundary)
            if bool(holes_list):
                holes = unary_union(holes_list)
                if 'hole' in self._regions:
                    self._regions['hole'] = self._regions['hole'].union(holes)
                else:
                    self._regions['hole'] = holes
        self._committed = True


    def collect_boundaries(self, **kwargs):
        if not self._committed:
            self.commit(**kwargs)
        boundaries = [self._roi.boundary]
        for pp in self._regions.values():
            boundaries.append(pp.boundary)
        return linemerge(unary_union(boundaries))


    def collect_region_markers(self, **kwargs):
        """get a arbitrary maker point for each connected region"""
        if not self._committed:
            self.commit(**kwargs)
        points = {}
        points['default'] = get_polygon_representative_point(self._roi)
        for lbl, pp in self._regions.items():
            points[lbl] = get_polygon_representative_point(pp)
        return points


    def simplify(self, region_tol=1.5, roi_tol=1.5, inplace=True):
        """
        simplify regions and roi so they have fewer line segments.
        Kwargs:
            region_tol(dict or scalar): maximum tolerated distance bwteen the
                points on the simplified regions and the unsimplified version.
                Could be a scalar that decines the universal behavior, or a dict
                to specify the tolerance for each region key.
            roi_tol(scalar): maximum tolerated distance for outer roi boundary.
        """
        if self._committed:
            import warnings
            warnings.warn('Geometry alread commited. Simplification aborted', RuntimeWarning)
            return self
        if not isinstance(region_tol, dict):
            region_tols = defaultdict(lambda: region_tol)
        else:
            region_tols = region_tol
        regions_new = {}
        for key, pp in self._regions.items():
            if (region_tols[key] > 0) and (pp is not None):
                pp_updated = pp.simplify(region_tols[key], preserve_topology=True)
                if inplace:
                    self._regions[key] = pp_updated
                else:
                    regions_new[key] = pp_updated
        if roi_tol > 0:
            roi = self._roi.simplify(roi_tol, preserve_topology=True)
            if inplace:
                self._roi = roi
        if inplace:
            return self
        else:
            return Geometry(roi=roi, regions=regions_new,
                resolution=self._resolution, zorder=self._zorder)


    def PSLG(self, **kwargs):
        """
        generate a Planar Straight Line Graph representation of the geometry to
        feed to the triangulator library.
        Kwargs:
            simplify_region_tol, simplify_roi_tol: distance tolerances passed to
                self.simplify.
            area_thresh: area minimum threshold passed to self.commit.
            snap_decimal: decimal number to round the coordinates so that close
                points would snap together
        Return:
            vertices (Nx2 np.ndarray): vertices of PSLG
            segments (Mx2 np.ndarray): list of endpoints' vertex id for each
                segment of PSLG
            markers (dict of lists): marker points for each region names.
        """
        simplify_region_tol = kwargs.get('simplify_region_tol', 0)
        simplify_roi_tol = kwargs.get('simplify_roi_tol', 0)
        area_thresh = kwargs.get('area_thresh', 0)
        snap_decimal = kwargs.get('snap_decimal', None)
        if (simplify_region_tol > 0) or (simplify_roi_tol > 0):
            self.simplify(region_tol=simplify_region_tol, roi_tol=simplify_roi_tol, inplace=True)
        self.commit(area_thresh=area_thresh)
        boundaries = self.collect_boundaries()
        markers = self.collect_region_markers()
        if hasattr(boundaries, 'geoms'):
            vertices_staging = []
            segments_staging = []
            crnt_len = 0
            for linestr in boundaries.geoms:
                xy = np.asarray(linestr.coords)
                Npt = xy.shape[0]
                vertices_staging.append(xy)
                seg = np.stack((np.arange(Npt-1), np.arange(1, Npt)), axis=-1) + crnt_len
                segments_staging.append(seg)
                crnt_len += Npt
            vertices = np.concatenate(vertices_staging, axis=0)
            segments = np.concatenate(segments_staging, axis=0)
        else:
            vertices = np.asarray(boundaries.coords)
            Npt = vertices.shape[0]
            segments = np.stack((np.arange(Npt-1), np.arange(1, Npt)), axis=-1)
        if snap_decimal is not None:
            vertices = np.round(vertices, decimals=snap_decimal)
        vertices, indx = np.unique(vertices, return_inverse=True, axis=0)
        segments = indx[segments]
        return vertices, segments, markers


    @staticmethod
    def region_names_from_material_dict(material_dict):
        if isinstance(material_dict, str):
            if '.json' in material_dict:
                MT = material.MaterialTable.from_json(material_dict, stream=False)
            else:
                MT = material.MaterialTable.from_json(material_dict, stream=True)
            material_dict = MT.label_table
        elif isinstance(material_dict, material.MaterialTable):
            material_dict = material_dict.label_table
        elif isinstance(material_dict, dict):
            pass
        else:
            raise TypeError('Invalid material dictionary type.')
        region_names = OrderedDict()
        for label, mat in material_dict.items():
            if isinstance(mat, material.Material):
                matval = mat._mask_label
                if matval is None:
                    raise RuntimeError('material label not defined in material table.')
            else:
                matval = mat
            if isinstance(matval, int):
                region_names[label] = matval
            elif isinstance(matval, (list, tuple, np.ndarray)):
                region_names[label] = np.asarray(matval)
            else:
                raise TypeError('invalid material label value type.')
        return region_names
