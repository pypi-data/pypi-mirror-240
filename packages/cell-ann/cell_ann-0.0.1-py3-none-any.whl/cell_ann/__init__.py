# __init__.py

from ._logger import Logger as _LOGGER
from .__version__ import __version__

__logger__ = _LOGGER()

import pathlib as _pathlib

_pkg_path = _pathlib.Path(__file__).absolute()
__logger__.info(f"import cell-ann (version: {__version__})")
__logger__.info(f"source: {_pkg_path}")


from . import _core
from ._knn import kNN
