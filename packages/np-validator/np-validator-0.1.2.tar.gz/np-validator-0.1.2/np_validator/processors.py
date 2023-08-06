from typing import Any

import logging
import pickle
import sys

logger = logging.getLogger(__name__)

try:
    from .sync_dataset import Dataset
except ImportError as ie:
    if sys.version_info[1] < 8:  # numpy only supported for 3.8+
        logger.debug("Numpy not supported for python versions < 3.8")
    else:
        raise ie


def unpickle(filepath: str, encoding: str = "latin1") -> Any:
    with open(filepath, "rb") as f:
        return pickle.load(f, encoding=encoding)  # nosec


def load_data_set(filepath: str) -> Dataset:
    return Dataset(filepath)
