from abc import ABC, abstractmethod
from collections import OrderedDict
from functools import partial
import glob
import json
import os
import re

import cv2
import numpy as np
from rtree import index

from feabas.miscs import generate_cache, crop_image_from_bbox


# bbox :int: [xmin, ymin, xmax, ymax]

##------------------------------ tile dividers -------------------------------##
# tile divider functions to divide an image tile to smaller block for caching
# Args:
#    imght, imgwd (int): height/width of image bounding box
#    x0, y0 (int): x, y coordinates of top-left conrer of image bounding box
# Returns:
#    divider: dict[block_id] = [xmin, ymin, xmax, ymax]
# Tiles with tile_id <=0 will not be cached. (DynamicImageLoader._cache_block)

def _tile_divider_blank(imght, imgwd, x0=0, y0=0):
    """Cache image as a whole without division."""
    divider = OrderedDict()
    divider[1] = (x0, y0, x0+imgwd, y0+imght)
    return divider


def _tile_divider_border(imght, imgwd, x0=0, y0=0, cache_border_margin=10):
    """Divide image borders to cache separately. Interior is not cached."""
    divider = OrderedDict()
    if cache_border_margin == 0:
        divider[1] = (x0, y0, x0+imgwd, y0+imght)
    else:
        border_ht = min(cache_border_margin, imght // 2)
        border_wd = min(cache_border_margin, imgwd // 2)
        x1, x2, x3, x4 = 0, border_wd, (imgwd - border_wd), imgwd
        y1, y2, y3, y4 = 0, border_ht, (imght - border_ht), imght
        # start from the interior (not cached) so it appears earlier in rtree
        if (x2 < x3) and (y2 < y3):
            divider[0] = (x2 + x0, y2 + y0, x3 + x0, y3 + y0)
        divider.update({
            1: (x1 + x0, y1 + y0, x3 + x0, y2 + y0),
            2: (x1 + x0, y2 + y0, x2 + x0, y4 + y0),
            3: (x2 + x0, y3 + y0, x4 + x0, y4 + y0),
            4: (x3 + x0, y1 + y0, x4 + x0, y3 + y0),
        })
    return divider


def _tile_divider_block(imght, imgwd, x0=0, y0=0, cache_block_size=0):
    """Divide image to equal(ish) square(ish) blocks to cache separately."""
    divider = OrderedDict()
    if cache_block_size == 0:
        divider[1] = (x0, y0, x0+imgwd, y0+imght)
    else:
        Nx = max(round(imgwd / cache_block_size), 1)
        Ny = max(round(imght / cache_block_size), 1)
        xx = np.round(np.linspace(x0, x0+imgwd, Nx+1)).astype(int)
        yy = np.round(np.linspace(y0, y0+imght, Ny+1)).astype(int)
        xe0, ye0 = np.meshgrid(xx[:-1], yy[:-1])
        xe1, ye1 = np.meshgrid(xx[1:], yy[1:])
        xe0 = xe0.ravel()
        ye0 = ye0.ravel()
        xe1 = xe1.ravel()
        ye1 = ye1.ravel()
        indx = np.argsort(xe0 + ye0 + xe1 + ye1, axis=None)
        key = 1
        for xmin, ymin, xmax, ymax in zip(xe0[indx], ye0[indx], xe1[indx], ye1[indx]):
            divider[key] = (xmin, ymin, xmax, ymax)
            key += 1
    return divider


##------------------------------ image loaders -------------------------------##

class AbstractImageLoader(ABC):
    """
    Abstract class for image loader.
    Kwargs:
        dtype: datatype of the output images. Default to None same as input.
        number_of_channels: # of channels of the output images. Default to
            None same as input.
        apply_CLAHE(bool): whether to apply CLAHE on output images.
        inverse(bool): whether to invert images.
        fillval(scalar): fill value for missing data.
        cache_size(int): length of image cache.
        cache_border_margin(int)/cache_block_size(int): the border width
            for _tile_divider_border caching, or the square block size for
            _tile_divider_block caching. If neither is set, cache
            the entile image with _tile_divider_blank.
        resolution(float): resolution of the images. default to 4nm
    """
    def __init__(self, **kwargs):
        self._dtype = kwargs.get('dtype', None)
        self._number_of_channels = kwargs.get('number_of_channels', None)
        self._apply_CLAHE = kwargs.get('apply_CLAHE', False)
        self._CLAHE = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        self._inverse = kwargs.get('inverse', False)
        self._default_fillval = kwargs.get('fillval', 0)
        self._cache_size = kwargs.get('cache_size', 0)
        self._use_cache = (self._cache_size is None) or (self._cache_size > 0)
        self._init_tile_divider(**kwargs)
        self._cache_type = kwargs.get('cache_type', 'mfu')
        self._cache = generate_cache(self._cache_type, maxlen=self._cache_size)
        self.resolution = kwargs.get('resolution', 4.0)


    def clear_cache(self, instant_gc=False):
        # instant_gc: when True, instantly call garbage collection
        self._cache.clear(instant_gc)


    def CLAHE_off(self):
        if self._apply_CLAHE:
            self.clear_cache()
            self._apply_CLAHE = False


    def CLAHE_on(self):
        if not self._apply_CLAHE:
            self.clear_cache()
            self._apply_CLAHE = True


    def inverse_off(self):
        if self._inverse:
            self.clear_cache()
            self._inverse = False


    def inverse_on(self):
        if not self._inverse:
            self.clear_cache()
            self._inverse = True


    def save_to_json(self, jsonname, **kwargs):
        out = {'ImageLoaderType': self.__class__.__name__}
        out.update(self._export_dict(**kwargs))
        with open(jsonname, 'w') as f:
            json.dump(out, f, indent=2)


    def _cached_block_rtree_generator(self, bbox):
        x0 = bbox[0]
        y0 = bbox[1]
        imght = bbox[3] - bbox[1]
        imgwd = bbox[2] - bbox[0]
        for blkid, blkbbox in self._tile_divider(imght, imgwd, x0=x0, y0=y0).items():
            yield (blkid, blkbbox, None)


    def _crop_from_one_image(self, bbox, imgpath, return_empty=False, return_index=False, **kwargs):
        fillval = kwargs.get('fillval', self._default_fillval)
        dtype = kwargs.get('dtype', self.dtype)
        number_of_channels = kwargs.get('number_of_channels', self.number_of_channels)
        if (not self._use_cache) or (imgpath not in self._cache):
            imgout = self._crop_from_one_image_without_cache(bbox, imgpath, return_empty=return_empty, return_index=return_index, **kwargs)
        else:
            # find the intersection between crop bbox and cached block bboxes
            bbox_img = self._get_image_bbox(imgpath)
            hits = self._get_image_hits(imgpath, bbox)
            if not hits:
                # no overlap, return trivial results based on output control
                if return_empty and not return_index:
                    if dtype is None or number_of_channels is None:
                      # not sufficient info to generate empty tile, read an image to get info
                        img = self._read_image(imgpath, **kwargs)
                        imgout = crop_image_from_bbox(img, bbox_img, bbox, return_index=False,
                            return_empty=True, fillval=fillval)
                    else:
                        outht = bbox[3] - bbox[1]
                        outwd = bbox[2] - bbox[0]
                        if number_of_channels <= 1:
                            outsz = (outht, outwd)
                        else:
                            outsz = (outht, outwd, number_of_channels)
                        imgout = np.full(outsz, fillval, dtype=dtype)
                elif return_index:
                    imgout = None, None
                else:
                    imgout = None
            elif any(item not in self._get_cached_dict(imgpath) for item in hits):
                # has missing blocks from cache, need to read image anyway
                imgout = self._crop_from_one_image_without_cache(bbox, imgpath, return_empty=return_empty, return_index=return_index, **kwargs)
            else:
                # read from cache
                if return_index:
                    px_max, py_max, px_min, py_min  = bbox_img
                    for bbox_blk in hits.values():
                        tx_min, ty_min, tx_max, ty_max = [int(s) for s in bbox_blk]
                        px_min = min(px_min, tx_min)
                        py_min = min(py_min, ty_min)
                        px_max = max(px_max, tx_max)
                        py_max = max(py_max, ty_max)
                    bbox_partial = (px_min, py_min, px_max, py_max)
                else:
                    bbox_partial = bbox
                initialized = False
                cache_dict = self._get_cached_dict(imgpath)
                for blkid, blkbbox in hits.items():
                    blkbbox = [int(s) for s in blkbbox]
                    blk = cache_dict[blkid]
                    if blk is None:
                        continue
                    if not initialized:
                        imgp = crop_image_from_bbox(blk, blkbbox, bbox_partial,
                            return_index=False, return_empty=True, fillval=fillval)
                        initialized = True
                    else:
                        blkt, indx =  crop_image_from_bbox(blk, blkbbox, bbox_partial,
                            return_index=True, return_empty=False, fillval=fillval)
                        if indx is not None and blkt is not None:
                            imgp[indx] = blkt
                if return_index:
                    imgout = crop_image_from_bbox(imgp, bbox_partial, bbox, return_index=True,
                        return_empty=return_empty, fillval=fillval)
                else:
                    imgout = imgp
        return imgout


    def _crop_from_one_image_without_cache(self, bbox, imgpath, return_empty=False, return_index=False, **kwargs):
        # directly crop the image without checking the cache first
        fillval = kwargs.get('fillval', self._default_fillval)
        img = self._read_image(imgpath, **kwargs)
        bbox_img = self._get_image_bbox(imgpath)
        imgout = crop_image_from_bbox(img, bbox_img, bbox, return_index=return_index,
            return_empty=return_empty, fillval=fillval)
        if self._use_cache:
            self._cache_image(imgpath, img=img, **kwargs)
        return imgout


    def _settings_dict(self, **kwargs):
        output_controls = kwargs.get('output_controls', True)
        cache_settings = kwargs.get('cache_settings', True)
        out = {}
        out['resolution'] = self.resolution
        if output_controls:
            if self._dtype is not None:
                out['dtype'] = np.dtype(self._dtype).str
            if self._number_of_channels is not None:
                out['number_of_channels'] = self._number_of_channels
            out['fillval'] = self._default_fillval
            out['apply_CLAHE'] = self._apply_CLAHE
            out['inverse'] = self._inverse
        if cache_settings:
            out['cache_size'] = self._cache_size
            out['cache_type'] = self._cache_type
            if self._tile_divider_type == 'border':
                out['cache_border_margin'] = self._cache_border_margin
            elif self._tile_divider_type == 'block':
                out['cache_block_size'] = self.cache_block_size
        return out


    def _init_tile_divider(self, **kwargs):
        if not self._use_cache:
            self._tile_divider = _tile_divider_blank
            self._tile_divider_type = 'blank'
        elif 'cache_border_margin' in kwargs:
            self._tile_divider = partial(_tile_divider_border, cache_border_margin=kwargs['cache_border_margin'])
            self._tile_divider_type = 'border'
        elif 'cache_block_size' in kwargs:
            self._tile_divider = partial(_tile_divider_block, cache_block_size=kwargs['cache_block_size'])
            self._tile_divider_type = 'block'
        else:
            self._tile_divider = _tile_divider_blank
            self._tile_divider_type = 'blank'


    @staticmethod
    def _load_settings_from_json(jsonname):
        with open(jsonname, 'r') as f:
            json_obj = json.load(f)
        settings = {}
        if 'resolution' in json_obj:
            settings['resolution'] = json_obj['resolution']
        if 'dtype' in json_obj:
            settings['dtype'] = np.dtype(json_obj['dtype'])
        if 'number_of_channels' in json_obj:
            settings['number_of_channels'] = int(json_obj['number_of_channels'])
        if 'fillval' in json_obj:
            settings['fillval'] = json_obj['fillval']
        if 'apply_CLAHE' in json_obj:
            settings['apply_CLAHE'] = json_obj['apply_CLAHE']
        if 'inverse' in json_obj:
            settings['inverse'] = json_obj['inverse']
        if 'cache_size' in json_obj:
            settings['cache_size'] = json_obj['cache_size']
        if 'cache_type' in json_obj:
            settings['cache_type'] = json_obj['cache_type']
        if 'cache_border_margin' in json_obj:
            settings['cache_border_margin'] = json_obj['cache_border_margin']
        elif 'cache_block_size' in json_obj:
            settings['cache_block_size'] = json_obj['cache_block_size']
        return settings, json_obj


    def _read_image(self, imgpath, **kwargs):
        number_of_channels = kwargs.get('number_of_channels', self._number_of_channels)
        dtype = kwargs.get('dtype', self._dtype)
        apply_CLAHE = kwargs.get('apply_CLAHE', self._apply_CLAHE)
        inverse = kwargs.get('inverse', self._inverse)
        if number_of_channels == 3:
            img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
        else:
            img = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED)
        if img is None:
            invalid_image_file_error = 'Image file {} not valid!'.format(imgpath)
            raise RuntimeError(invalid_image_file_error)
        if (number_of_channels == 1) and (len(img.shape) > 2) and (img.shape[-1] > 1):
            img = img.mean(axis=-1)
        if dtype is not None:
            img = img.astype(dtype, copy=False)
        if apply_CLAHE:
            img = self._CLAHE.apply(img)
        if inverse:
            if np.dtype(dtype) == np.dtype('uint8'):
                img = 255 - img
            elif np.dtype(dtype) == np.dtype('uint16'):
                img = 65535 - img
            else:
                img = img.max() - img
        return img


    def _export_dict(self, **kwargs):
        """turn the loader settings to a dict used in self.save_to_json"""
        return self._settings_dict(**kwargs)


    @abstractmethod
    def _get_cached_dict(self, imgpath):
        """cached_dict get function used in self._crop_from_one_image"""
        pass


    @abstractmethod
    def _get_image_bbox(self, imgpath):
        """image_bbox get function used in self._crop_from_one_image"""
        pass


    @abstractmethod
    def _get_image_cached_block_rtree(self, imgpath):
        """image_cached_block_rtree get function used in self._crop_from_one_image"""
        pass

    
    def _get_image_hits(self, imgpath, bbox):
        # hits[blkid] = bbox
        cached_block_rtree = self._get_image_cached_block_rtree(imgpath)
        hit_list = list(cached_block_rtree.intersection(bbox, objects=True))
        hits ={item.id: item.bbox for item in hit_list}
        return hits


    @property
    def number_of_channels(self):
        return self._number_of_channels


    @property
    def dtype(self):
        return self._dtype



class DynamicImageLoader(AbstractImageLoader):
    """
    Class for image loader without predetermined image list.
    Mostly for caching & output formate control.
    caching format:
        self._cache[imgpath] = ((0,0,imgwd, imght), cache_dict{blkid: tile})
        self._cached_block_rtree[(imght, imgwd)] = rtree
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._cached_block_rtree = {}


    def crop(self, bbox, imgpath, return_empty=False, return_index=False, **kwargs):
        return super()._crop_from_one_image(bbox, imgpath, return_empty=return_empty, return_index=return_index, **kwargs)


    @classmethod
    def from_json(cls, jsonname, **kwargs):
        settings, _ = cls._load_settings_from_json(jsonname)
        settings.update(kwargs)
        return cls(**settings)


    def _cache_image(self, imgpath, img=None, **kwargs):
        # self._cache[imgpath] = ((0, 0, imgwd, imght), cache_dict{blkid: tile})
        if not self._use_cache:
            return
        if imgpath in self._cache:
            cache_dict = self._cache[imgpath]
            bbox_img = cache_dict[0]
            x0, y0, x1, y1 = bbox_img
            imgwd = x1 - x0
            imght = y1 - y0
        else:
            cache_dict = {}
            if img is None:
                img = self._read_image(imgpath, **kwargs)
            imght = img.shape[0]
            imgwd = img.shape[1]
            x0 = 0
            y0 = 0
            bbox_img = (x0, y0, x0+imgwd, y0+imght)
        if bbox_img not in self._cached_block_rtree:
            self._cached_block_rtree[bbox_img] = index.Index(
                self._cached_block_rtree_generator(bbox_img), interleaved=True)
        divider = self._tile_divider(imght, imgwd, x0=x0, y0=y0)
        new_cache = False
        for bid, blkbbox in divider.items():
            if (bid > 0) and (bid not in cache_dict):
                if img is None:
                    img = self._read_image(imgpath, **kwargs)
                blk = img[blkbbox[1]:blkbbox[3], blkbbox[0]:blkbbox[2],...]
                cache_dict[bid] = blk
                new_cache = True
        if new_cache:
            self._cache[imgpath] = ((0, 0, imgwd,imght), cache_dict)


    def _get_cached_dict(self, imgpath):
        if imgpath not in self._cache:
            image_not_in_cache = '{} not in the image loader cache'.format(imgpath)
            raise KeyError(image_not_in_cache)
        else:
            return self._cache[imgpath][1]


    def _get_image_bbox(self, imgpath):
        if imgpath in self._cache:
            return self._cache[imgpath][0]
        else:
            img = self._read_image(imgpath)
            imght = img.shape[0]
            imgwd = img.shape[1]
            return (0,0, imgwd, imght)


    def _get_image_cached_block_rtree(self, imgpath):
        bbox_img = self._get_image_bbox(imgpath)
        if bbox_img not in self._cached_block_rtree:
            self._cached_block_rtree[bbox_img] = index.Index(
                    self._cached_block_rtree_generator(bbox_img), interleaved=True)
        return self._cached_block_rtree[bbox_img]



class StaticImageLoader(AbstractImageLoader):
    """
    Class for image loader with predetermined image list.
    Assuming all the images are of the same dimensions dtype and bitdepth.

    Args:
        filepaths(list): fullpaths of the image file list
    Kwargs:
        tile_size(tuple): the size of tiles.
            If None(default), infer from the first image encountered.
    caching format:
        self._cache[imgpath] = cache_dict{blkid: tile}
        self._cached_block_rtree = rtree
    """
    def __init__(self, filepaths, **kwargs):
        super().__init__(**kwargs)
        self.imgrootdir = os.path.dirname(os.path.commonprefix(filepaths))
        self.imgrelpaths = [os.path.relpath(s, self.imgrootdir) for s in filepaths]
        self.check_filename_uniqueness()
        self._tile_size = kwargs.get('tile_size', None)
        self._cached_block_rtree = {}
        self._divider = None


    def check_filename_uniqueness(self):
        assert(len(self.imgrelpaths) > 0), 'empty file list'
        assert len(set(self.imgrelpaths)) == len(self.imgrelpaths), 'duplicated filenames'


    def crop(self, bbox, fileid, return_empty=False, return_index=False, **kwargs):
        if isinstance(fileid, str):
            filepath = fileid
            fileid = self.fileid_lookup(filepath)
        return super()._crop_from_one_image(bbox, fileid, return_empty=return_empty, return_index=return_index, **kwargs)


    @classmethod
    def from_json(cls, jsonname, **kwargs):
        settings, json_obj = cls._load_settings_from_json(jsonname)
        filepaths = []
        if 'tile_size' in json_obj:
            settings['tile_size'] = json_obj['tile_size']
        settings.update(kwargs)
        for f in json_obj['images']:
            filepaths.append(f['filepath'])
        return cls(filepaths=filepaths, **settings)


    def _cache_image(self, fileid, img=None, **kwargs):
        if not self._use_cache:
            return
        if isinstance(fileid, str):
            filepath = fileid
            fileid = self.fileid_lookup(filepath)
            if fileid == -1:
                image_not_in_list = '{} not in the image loader list'.format(filepath)
                raise KeyError(image_not_in_list)
        if fileid in self._cache:
            cache_dict = self._cache[fileid]
        else:
            cache_dict = {}
        new_cache = False
        for bid, blkbbox in self.divider.items():
            if (bid > 0) and (bid not in cache_dict):
                if img is None:
                    img = self._read_image(fileid, **kwargs)
                blk = img[blkbbox[1]:blkbbox[3], blkbbox[0]:blkbbox[2],...]
                cache_dict[bid] = blk
                new_cache = True
        if new_cache:
            self._cache[fileid] = cache_dict


    def _export_dict(self, output_controls=True, cache_settings=True, image_list=True):
        out = super()._settings_dict(output_controls=output_controls, cache_settings=cache_settings)
        if self._tile_size is not None:
            out['tile_size'] = self._tile_size
        if image_list:
            out['images'] = [{'filepath':s} for s in self.filepaths_generator]
        return out


    def _get_cached_dict(self, fileid):
        if fileid not in self._cache:
            if isinstance(fileid, str):
                imgpath = fileid
            else:
                imgpath = os.path.join(self.imgrootdir, self.imgrelpaths[fileid])
            imgpath = os.path.join(self.imgrootdir, self.imgrelpaths[fileid])
            image_not_in_cache = '{} not in the image loader cache'.format(imgpath)
            raise KeyError(image_not_in_cache)
        else:
            return self._cache[fileid]


    def _get_image_bbox(self, fileid):
        imght, imgwd = self.tile_size
        return (0,0, imgwd, imght)


    def _get_image_cached_block_rtree(self, fileid):
        tile_ht, tile_wd = self.tile_size
        bbox_img = (0, 0, tile_wd, tile_ht)
        return self.cached_block_rtree[bbox_img]


    def _read_image(self, fileid, **kwargs):
        if isinstance(fileid, str):
            imgpath = fileid
        else:
            imgpath = os.path.join(self.imgrootdir, self.imgrelpaths[fileid])
        img = super()._read_image(imgpath, **kwargs)
        if self._tile_size is None:
            self._tile_size = img.shape[:2]
        tile_ht, tile_wd = self._tile_size
        bbox_img = (0, 0, tile_wd, tile_ht)
        if bbox_img not in self._cached_block_rtree:
            self._cached_block_rtree[bbox_img] = index.Index(
                self._cached_block_rtree_generator(bbox_img), interleaved=True)
        if self._divider is None:
            tile_ht, tile_wd = self._tile_size
            self._divider = self._tile_divider(tile_ht, tile_wd, x0=0, y0=0)
        if self._dtype is None:
            self._dtype = img.dtype
        if self._number_of_channels is None:
            if len(img.shape) <= 2:
                self._number_of_channels = 1
            else:
                self._number_of_channels = img.shape[-1]
        return img


    def fileid_lookup(self, fname):
        if (not hasattr(self, '_fileid_LUT')) or (self._fileid_LUT is None):
            self._fileid_LUT = {}
            for idx, fnm in enumerate(self.filepaths_generator):
                self._fileid_LUT[fnm] = idx
        if fname in self._fileid_LUT:
            return self._fileid_LUT[fname]
        else:
            return -1


    @property
    def cached_block_rtree(self):
        if self._cached_block_rtree is None:
            self._read_image(0)
        return self._cached_block_rtree


    @property
    def divider(self):
        if self._divider is None:
            self._read_image(0)
        return self._divider


    @property
    def dtype(self):
        if self._dtype is None:
            self._read_image(0)
        return self._dtype


    @property
    def filepaths_generator(self):
        for fname in self.imgrelpaths:
            yield os.path.join(self.imgrootdir, fname)


    @property
    def filepaths(self):
        return list(self.filepaths_generator)


    @property
    def number_of_channels(self):
        if self._number_of_channels is None:
            self._read_image(0)
        return self._number_of_channels


    @property
    def tile_size(self):
        if self._tile_size is None:
            self._read_image(0)
        return self._tile_size



class MosaicLoader(StaticImageLoader):
    """
    Image loader to render cropped images from non-overlapping tiles
        bbox :int: [xmin, ymin, xmax, ymax]
    """
    def __init__(self, filepaths, bboxes, **kwargs):
        assert len(filepaths) == len(bboxes)
        super().__init__(filepaths, **kwargs)
        self._file_bboxes = bboxes
        self._init_rtrees()


    @classmethod
    def from_filepaths(cls, imgpaths, pattern='_tr(\d+)-tc(\d+)', rc_offset=[1, 1], rc_order=True, **kwargs):
        """
        pattern:    regexp pattern to parse row-column pattern
        rc_offset:  if None, normalize
        rc_order:   True:row-colume or False:colume-row
        """
        tile_size = kwargs.get('tile_size', None)   # if None, read in first image
        if isinstance(imgpaths, str):
            if '*' in imgpaths:
                imgpaths = glob.glob(imgpaths)
                assert bool(imgpaths), 'No image found: {}'.format(imgpaths)
                imgpaths.sort()
            else:
                imgpaths = [imgpaths]
        if len(imgpaths) == 1:
            r_c = np.array([(0, 0)])
        else:
            r_c = np.array([MosaicLoader._filename_parser(s, pattern, rc_order=rc_order) for s in imgpaths])
            if rc_offset is None:
                r_c -= r_c.min(axis=0)
            else:
                r_c -= np.array(rc_offset).reshape(1,2)
        if tile_size is None:
            img = cv2.imread(imgpaths[0], cv2.IMREAD_UNCHANGED)
            imght, imgwd = img.shape[0], img.shape[1]
            tile_size = (imght, imgwd)
        bboxes = []
        for rc in r_c:
            r = rc[0]
            c = rc[1]
            bbox = [c*tile_size[1], r*tile_size[0], (c+1)*tile_size[1], (r+1)*tile_size[0]]
            bboxes.append(bbox)
        return cls(filepaths=imgpaths, bboxes=bboxes, **kwargs)


    @classmethod
    def from_json(cls, jsonname, **kwargs):
        settings, json_obj = cls._load_settings_from_json(jsonname)
        settings.update(kwargs)
        filepaths = []
        bboxes = []
        for f in json_obj['images']:
            filepaths.append(f['filepath'])
            bboxes.append(f['bbox'])
        return cls(filepaths=filepaths, bboxes=bboxes, **settings)


    def _file_rtree_generator(self):
        """
        generator function to build rtree of image bounding boxes.
        """
        for fileid, bbox in enumerate(self._file_bboxes):
            yield (fileid, bbox, None)


    def crop(self, bbox, return_empty=False, **kwargs):
        hits = self._file_rtree.intersection(bbox, objects=False)
        initialized = False
        if hits:
            for fileid in hits:
                if not initialized:
                    out = super().crop(bbox, fileid, return_empty=return_empty, return_index=False, **kwargs)
                    if out is not None:
                        initialized = True
                else:
                    blk, indx = super().crop(bbox, fileid, return_empty=return_empty, return_index=True, **kwargs)
                    if blk is not None:
                        out[indx] = blk
        else:
            if return_empty:
                out = super().crop(bbox, 0, return_empty=True, return_index=False, **kwargs)
            else:
                out = None
        return out


    def file_bboxes(self, margin=0):
        for bbox in self._file_bboxes:
            bbox_m = [bbox[0]-margin, bbox[1]-margin, bbox[2]+margin, bbox[3]+margin]
            yield bbox_m


    def _export_dict(self, output_controls=True, cache_settings=True, image_list=True):
        out = super()._settings_dict(output_controls=output_controls, cache_settings=cache_settings)
        if image_list:
            out['images'] = [{'filepath':p, 'bbox':b} for p, b in zip(self.filepaths_generator, self._file_bboxes)]
        return out


    def _get_image_bbox(self, fileid):
        if isinstance(fileid, str):
            filepath = fileid
            fileid = self.fileid_lookup(filepath)
            if fileid == -1:
                image_not_in_list = '{} not in the image loader list'.format(filepath)
                raise KeyError(image_not_in_list)
        return self._file_bboxes[fileid]


    def _get_image_cached_block_rtree(self, fileid):
        bbox_img = self._get_image_bbox(fileid)
        xmin, ymin, xmax, ymax = bbox_img
        # normalize bbox to reduce number of rtrees needed
        bbox_normalized = (0, 0, xmax - xmin, ymax - ymin)
        if bbox_normalized not in self._cached_block_rtree:
            self._cached_block_rtree[bbox_normalized] = index.Index(
                    self._cached_block_rtree_generator(bbox_normalized), interleaved=True)
        return self._cached_block_rtree[bbox_normalized]


    def _get_image_hits(self, fileid, bbox):
        # hits[blkid] = bbox
        imgbbox = self._get_image_bbox(fileid)
        xmin_img, ymin_img, _, _ = imgbbox
        bbox_normalized = (bbox[0]-xmin_img, bbox[1]-ymin_img,
            bbox[2]-xmin_img, bbox[3]-ymin_img)
        cached_block_rtree_normalized = self._get_image_cached_block_rtree(fileid)
        hit_list = list(cached_block_rtree_normalized.intersection(bbox_normalized, objects=True))
        hits = {}
        for item in hit_list:
            bbox_hit = item.bbox
            bbox_out = (bbox_hit[0]+xmin_img, bbox_hit[1]+ymin_img,
                bbox_hit[2]+xmin_img, bbox_hit[3]+ymin_img)
            hits[item.id] = bbox_out
        return hits


    def _init_rtrees(self):
        self._file_rtree = index.Index(self._file_rtree_generator(), interleaved=True)
        self._cache_block_rtree = {}
        for bbox in self._file_bboxes:
            # normalize file bounding box to reduce number of trees needed
            imgwd = bbox[2] - bbox[0]
            imght = bbox[3] - bbox[1]
            box_normalized = (0, 0, imgwd, imght)
            if box_normalized not in self._cache_block_rtree:
                self._cache_block_rtree[box_normalized] = index.Index(
                    self._cached_block_rtree_generator(box_normalized), interleaved=True)


    @ staticmethod
    def _filename_parser(fname, pattern, rc_order=True):
        m = re.findall(pattern, fname)
        if rc_order:
            r = int(m[0][0])
            c = int(m[0][1])
        else:
            c = int(m[0][0])
            r = int(m[0][1])
        return r, c


    @property
    def bounds(self):
        return self._file_rtree.bounds
