# =============================================================================
# Imports
# =============================================================================
from pathlib import Path
from loguru import logger

from mth5.mth5 import MTH5
from mth5.helpers import close_open_files

# =============================================================================


def initialize_mth5(h5_path, mode="a", file_version="0.1.0"):
    """
    mth5 initializer for the case of writting files.


    :param h5_path: path to file
    :type h5_path: string or pathlib.Path
    :param mode: how to open the file, options are

        - "r": read
        - "w": write
        - "a": append

    :type mode: string
    :return: mth5 object
    :rtype: :class:`mth5.MTH5`


    """
    h5_path = Path(h5_path)
    if mode == "w":
        if h5_path.exists():
            logger.warning("File exists, removing from file system.")
            close_open_files()
            h5_path.unlink()
    mth5_obj = MTH5(file_version=file_version)
    mth5_obj.open_mth5(str(h5_path), mode=mode)

    return mth5_obj


def read_back_data(
    mth5_path,
    station_id,
    run_id,
    survey=None,
    close_mth5=True,
    return_objects=[],
):
    """
    Testing helper function, used to confirm that the h5 file can be accessed
    and that the data size is as expected.

    :param mth5_path: the full path the the mth5 that this method is going to
     try to read
    :type mth5_path: Path or string
    :param station_id: the label for the station, e.g. "PKD"
    :type station_id: string
    :param run_id: The label for the run to read.  e.g. "001"
    :type run_id: string
    :param survey: The label for the survey associated with the run to read.
    :type survey: string
    :param close_mth5: Whether or not to close the mth5 object after reading
    :type close_mth5: bool
    :param return_objects: List of strings.  Specifies what, if anything to return.
    Allowed values: ["run", "run_ts"]
    :type return_objects: List of strings.
    :return: run object
    :rtype: :class:`mth5.groups.RunGroup`
    :return: run time series
    :rtype: :class:`mth5.timeseries.RunTS`

    """
    processing_config = {}
    processing_config["mth5_path"] = str(mth5_path)
    processing_config["local_station_id"] = station_id
    config = processing_config
    m = initialize_mth5(config["mth5_path"], mode="r")
    local_run_obj = m.get_run(
        config["local_station_id"], run_id, survey=survey
    )
    local_run_ts = local_run_obj.to_runts()
    data_array = local_run_ts.dataset.to_array()
    logger.info(f"data shape = {data_array.shape}")

    return_dict = {}
    if "run" in return_objects:
        return_dict["run"] = local_run_obj
    if "run_ts" in return_objects:
        return_dict["run_ts"] = local_run_ts
    if close_mth5:
        m.close_mth5()
    else:
        return_dict["mth5_obj"] = m
    return return_dict


def get_compare_dict(input_dict):
    """
    Helper function for removing 2 added attributes to metadata

     - hdf5_reference
     - mth5_type

    :param input_dict: DESCRIPTION
    :type input_dict: TYPE
    :return: DESCRIPTION
    :rtype: TYPE

    """
    for key in ["hdf5_reference", "mth5_type"]:
        try:
            input_dict.pop(key)
        except KeyError:
            pass

    return input_dict
