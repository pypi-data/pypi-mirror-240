
import adata_query
import anndata
from . import __logger__
import numpy as np

from ._core import (
    BasekNN,
    SelfIDMixIn,
    NeighborQueryMixIn,
    MapQueryMixIn,
    CountBasedAssignmentMixIn,
)

class kNN(
    BasekNN,
    SelfIDMixIn,
    NeighborQueryMixIn,
    MapQueryMixIn,
    CountBasedAssignmentMixIn,
):
    def __init__(
        self,
        adata: anndata.AnnData,
        use_key: str = "X_pca",
        metric: str = "euclidean",
        n_neighbors: int = 20,
        n_trees: int = 10,
        type_check_enabled: bool = True,
        *args,
        **kwargs,
    ):
        super().__init__()

        __logger__.info(f"{self.__class__.__name__}.__init__")

        self.__parse__(locals())

        if not type_check_enabled:
            self._disable_type_check()

        self.__check_types__(func=self.__init__, passed=locals())
        self._build_annoy_index()
    
    def map_obs(
        self,
        X_query: np.ndarray,
        key: str,
        k_neighbors: int = 20,
        offset: int = 0,
        type_check_enabled: bool = True,
    ) -> np.ndarray:
        
        X_nn = self.neighbor_query(
            X_query=X_query, 
            k_neighbors=k_neighbors,
            offset=offset,
            type_check_enabled=type_check_enabled,
        )
                              
        return self.count_based_assignment(
            self.map_query(X_nn, attr_keys=key)[key], max_only=True
        )