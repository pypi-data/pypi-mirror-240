
import ABCParse
import anndata
import adata_query
import numpy as np
import pandas as pd

from typing import Dict, List, Union


class QueryMapper(ABCParse.ABCParse):
    """
    # NeighborRetriever
    Map retrieved neighbors to values in reference adata.

    With the neighbor indices in hand, one can retrieve
    reference adata attributes
    """

    def __init__(self, adata: anndata.AnnData, *args, **kwargs):
        self.__parse__(locals())

    @property
    def _FETCH_KWARGS(self):
        kwargs = self._PARAMS.copy()
        params_to_pop = ["args", "adata"]
        [kwargs.pop(param) for param in params_to_pop]
        return ABCParse.function_kwargs(func=adata_query.fetch, kwargs=kwargs)

    @property
    def flat_nn_idx(self):
        return self._X_nn.flatten()

    @property
    def _N(self):
        return len(self.flat_nn_idx)

    @property
    def _N_CELLS(self):
        return self._X_nn.shape[0]

    @property
    def _N_NEIGHBORS(self):
        return self._X_nn.shape[1]

    @property
    def nn_adata(self):
        """Setting this as an attribute enables fast recall of multiple items
        (e.g.; something from obs and "X_pca")"""
        if not hasattr(self, "_nn_adata"):
            self._nn_adata = self._adata[self.flat_nn_idx]
        return self._nn_adata

    def forward(self, key):
        X_fetch = adata_query.fetch(adata=self.nn_adata, key=key, **self._FETCH_KWARGS)
        if isinstance(X_fetch, pd.Series):
            X_fetch = X_fetch.to_numpy()
        return X_fetch.reshape(self._N_CELLS, self._N_NEIGHBORS, -1)  # )

    def __call__(
        self,
        X_nn: np.ndarray,
        attr_keys: Union[List[str], str],
        torch: bool = False,
        *args,
        **kwargs
    ) -> np.ndarray:
        """

        This part is meant to be flexible. Others can be more rigid.

        Parameters
        ----------
        X_nn: np.ndarray

        attr_keys: Union[List[str], str],

        torch: bool = False

        Returns
        -------
        """
        self.__update__(locals())

        return {key: self.forward(key) for key in ABCParse.as_list(attr_keys)}


def map_query(
    adata: anndata.AnnData, X_nn, attr_keys: Union[List[str], str]
) -> Dict[str, np.ndarray]:
    """
    This part is meant to be flexible (i.e., always returning a dictionary of
    np.ndarray of shape: n_cell x n_neighbors x n_dim_feature) Others can be more rigid.
    """
    qmap = QueryMapper(adata)
    return qmap(X_nn, attr_keys)


class MapQueryMixIn(object):
    def map_query(
        self, X_nn, attr_keys: Union[List[str], str]
    ) -> Dict[str, np.ndarray]:
        return map_query(adata=self._adata, X_nn=X_nn, attr_keys=attr_keys)