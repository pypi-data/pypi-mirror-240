# __init__.py

from ._logger import Logger as _LOGGER
from .__version__ import __version__

__logger__ = _LOGGER()

import pathlib

pkg_path = pathlib.Path(__file__).absolute()
__logger__.info(f"import cell-ann (version: {__version__})")
__logger__.info(f"source: {pkg_path}")

from ._neighbor_query import NeighborQuery, neighbor_query
from ._base_knn import BasekNN
from ._knn import kNN
from ._query_mapper import map_query
from ._value_counts_assignment import count_based_assignment