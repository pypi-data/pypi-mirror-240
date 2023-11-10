# coding=utf-8
import os.path
import uuid
import warnings
import shutil
from functools import wraps, partial
from tempfile import _candidate_tempdir_list
try:
    import pybedtools
except ImportError:
    raise ImportError("The region module in Pythonase requires a third-party package,"
                      " pybedtools, please install it first.")
import pandas as pd


def _set_pybedtools_tmp_dir(func=None, *, tmp_dir="."):
    if func is None:
        return partial(_set_pybedtools_tmp_dir, tmp_dir=tmp_dir)

    @wraps(func)  # use wraps to make sure the original doc string will be returned
    def wrapper(*args, **kwargs):
        prev_tmp_dir = pybedtools.get_tempdir()
        # check if the tempdir is modified before, if modified then leave it as it is
        # otherwise, use the working directory to avoid overwhelming the system's drive
        if not any([prev_tmp_dir.startswith(default_dir) for default_dir in _candidate_tempdir_list()]):
            pybdt_tmp = os.path.join(tmp_dir, "pybdt_" + str(uuid.uuid4()))
            if not os.path.exists(pybdt_tmp):
                os.mkdir(pybdt_tmp)
            pybedtools.set_tempdir(pybdt_tmp)

        # call the function
        ret = func(*args, **kwargs)
        return ret

    return wrapper


def _midpoint_generator(bed_regions):
    """
    Region midpoint generator

    Parameters
    ----------
    bed_regions : pybedtools.BedTool
        Regions in a BedTool object

    Yields
    -------

    """
    from pybedtools.featurefuncs import midpoint
    try:
        for region in bed_regions:
            yield midpoint(region)
    except Exception as e:
        warnings.warn(str(e), RuntimeWarning)


@_set_pybedtools_tmp_dir(tmp_dir=".")
def _midpoint_generator(bed_regions):
    """

    Parameters
    ----------
    bed_regions : pybedtools.BedTool

    Returns
    -------

    """
    from pybedtools.featurefuncs import midpoint
    try:
        for region in bed_regions:
            yield midpoint(region)
    except Exception as e:
        print(e)


@_set_pybedtools_tmp_dir(tmp_dir=".")
def extend_regions_from_mid_points(region, extensions, chromosome_size) -> pd.DataFrame:
    """
    Extend regions from their middle points

    Parameters
    ----------
    region : str or `pybedtools.BedTool` or `pd.DataFrame`
        Path to the region bed file, or a `BedTool` instance, or a `DataFrame` instance
    extensions : tuple of ints
        Two ints, first one for the upstream extension, the second one for the downstream extension
    chromosome_size : str
        Path to the chromosome size file or a name of genome release, like `hg38`.

    Returns
    -------
    extended_regions : `pd.DataFrame`
        Extended regions
    """
    if isinstance(region, pybedtools.BedTool):
        bed_obj = region
    elif isinstance(region, pd.DataFrame):
        bed_obj = pybedtools.BedTool.from_dataframe(region)
    elif isinstance(region, str) and os.path.exists(region):
        bed_obj = pybedtools.BedTool(region)
    else:
        raise ValueError("region is not supported")

    if not isinstance(chromosome_size, str):
        raise ValueError("chromosome_size must be a string")

    mid_points = pybedtools.BedTool(_midpoint_generator(bed_obj))
    if os.path.exists(chromosome_size) and os.path.isfile(chromosome_size):
        extended_regions = mid_points.slop(l=extensions[0], r=extensions[1], g=chromosome_size)
    else:
        extended_regions = mid_points.slop(l=extensions[0], r=extensions[1], genome=chromosome_size)
    return extended_regions.to_dataframe(disable_auto_names=True, header=None)
