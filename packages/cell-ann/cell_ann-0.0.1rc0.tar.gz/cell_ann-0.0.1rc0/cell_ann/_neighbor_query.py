
# -- import packages: ---------------------------------------------------------
import ABCParse
import adata_query
import annoy
import numpy as np


# -- import local dependencies: -----------------------------------------------
from ._type_check_mix_in import TypeCheckMixIn
from . import __logger__
from ._base_knn import BasekNN

from typing import List, Union


# -- operating class: ---------------------------------------------------------
class NeighborQuery(TypeCheckMixIn, ABCParse.ABCParse):
    def __init__(
        self,
        idx: annoy.AnnoyIndex,
        k_neighbors: int = 20,
        type_check_enabled: bool = True,
        *args,
        **kwargs
    ) -> None:
        
        """
        Parameters
        ----------
        idx: annoy.AnnoyIndex
        
        k_neighbors: int, default = 20
        
        type_check_enabled: bool, default = True
        
        Returns
        -------
        None
        """
        
        super().__init__()
        
        __logger__.info(f"{self.__class__.__name__}.__init__")
        
        self.__parse__(locals())
        self.__check_types__(func=self.__init__, passed=locals())
        
        if not type_check_enabled:
            self._disable_type_check()
            
    @property
    def k(self) -> int:
        return int(self._k_neighbors + self._offset)

    @property
    def _N_QUERY_CELLS(self) -> int:
        return self._X_query.shape[0]

    def _forward(self, X_query_i: np.ndarray) -> List:
        return self._idx.get_nns_by_vector(X_query_i, self.k)[self._offset:]
    
    def forward(self, X_query: np.ndarray) -> np.ndarray:
        return np.array([self._forward(X_query[i]) for i in range(self._N_QUERY_CELLS)])

    def __call__(self, X_query: np.ndarray, offset: int = 0) -> np.ndarray:
        """
        Match observed cells (X_query: np.ndarray) to their (k) nearest
        neighbors (X_nn: np.ndarray) in the given annoy idx.
        
        Parameters
        ----------
        X_query: np.ndarray
            Observations of size: [cells x n_dims].
            
        offset: int, default = 0
            Adds a pseudocount. Particularly useful for removing self-identifying cells.

        Returns
        -------
        X_nn: np.ndarray
            Neighbor assignments of size: [cells x n_neighbors].
        """

        __logger__.info(f"{self.__class__.__name__}.__call__")
        
        self.__update__(locals())
        self.__check_types__(func=self.__call__, passed=locals())
        
        return self.forward(X_query)


def _index_flatten(kNN: Union[annoy.AnnoyIndex, BasekNN]) -> annoy.AnnoyIndex:
    
    """Enable use of either cell_ann.kNN or annoy.AnnoyIndex
    
    Returns
    -------
    idx: annoy.AnnoyIndex
    """
    
    if isinstance(kNN, annoy.AnnoyIndex):
        return kNN
    elif isinstance(kNN, BasekNN):
        return kNN.idx
    
def neighbor_query(
    kNN: Union[annoy.AnnoyIndex, BasekNN],
    X_query: np.ndarray,
    k_neighbors: int = 20,
    offset: int = 0,
    type_check_enabled: bool = True,
) -> np.ndarray:
    """
    Parameters
    ----------
    kNN: Union[annoy.AnnoyIndex, BasekNN]
    
    X_query: np.ndarray
    
    k_neighbors: int = 20
    
    offset: int = 0
    
    type_check_enabled: bool = True
    
    
    Returns
    -------
    X_nn: np.ndarray
    """
    
    idx = _index_flatten(kNN)
        
    knn_query = NeighborQuery(
        idx=idx,
        k_neighbors=k_neighbors,
        type_check_enabled=type_check_enabled,
    )
    return knn_query(X_query=X_query, offset = offset)

class NeighborQueryMixIn(object):
    
    def neighbor_query(
        self: Union[annoy.AnnoyIndex, BasekNN],
        X_query: np.ndarray,
        k_neighbors: int = 20,
        offset: int = 0,
        type_check_enabled: bool = True,
    ) -> np.ndarray:
        """
        
        """
        return neighbor_query(
            kNN=self,
            X_query=X_query,
            k_neighbors=k_neighbors,
            offset=offset,
            type_check_enabled=type_check_enabled,
        )
