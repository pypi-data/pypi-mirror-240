
import ABCParse
import adata_query
import anndata
import annoy
import numpy as np
import time

from ._type_check_mix_in import TypeCheckMixIn
from .. import __logger__


from typing import Union
        
class BasekNN(TypeCheckMixIn, ABCParse.ABCParse):
    _IDX_BUILT = False

    def __init__(self, *args, **kwargs):
        
        super().__init__()
        
        __logger__.info(f"{self.__class__.__name__}.__init__")


    @property
    def _X_basis(self) -> np.ndarray:
        """Basis data on which the graph is built."""
        if not hasattr(self, "_X_basis_ATTR"):
            self._X_basis_ATTR = adata_query.fetch(
                self._adata, key=self._use_key, torch=False
            )
        return self._X_basis_ATTR

    @property
    def _N_CELLS(self) -> int:
        return self._X_basis.shape[0]

    @property
    def _N_DIMS(self) -> int:
        return self._X_basis.shape[1]

    def _build_annoy_index(self) -> annoy.AnnoyIndex:
        
        __logger__.info("Start kNN build")
        
        self._start_build_time = time.time()

        idx = annoy.AnnoyIndex(self._N_DIMS, self._metric)
        [idx.add_item(i, self._X_basis[i]) for i in range(self._N_CELLS)]
        idx.build(self._n_trees)
        self._idx = idx
        self._IDX_BUILT = True

        self._end_build_time = time.time()
        
        __logger__.info("End kNN build")

    @property
    def _BUILD_TIME(self) -> str:
        if not hasattr(self, "_build_time"):
            self._build_time = self._end_build_time - self._start_build_time
            self._print_build_time = "{:.4f} s".format(self._build_time)
            __logger__.info(f"kNN build time: {self._print_build_time}")
        return self._print_build_time

    @property
    def _BUILD_TIME_PER_CELL(self) -> str:
        self._print_build_time_per_cell = "{:.2e} s".format(self._build_time / self._N_CELLS)
        __logger__.info(f"kNN build time per cell: {self._print_build_time_per_cell}")
        return self._print_build_time_per_cell

    @property
    def idx(self) -> annoy.AnnoyIndex:
        """The actual annoy.AnnoyIndex"""

        if not hasattr(self, "_idx"):
            self._build_annoy_index()
        return self._idx

    def __repr__(self):
        return f"kNN: {self._use_key}, {self._N_CELLS} cells"
