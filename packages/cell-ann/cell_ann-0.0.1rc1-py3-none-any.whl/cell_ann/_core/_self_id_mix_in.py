
import numpy as np
import adata_query


class SelfIDMixIn(object):
    @property
    def _NN_0_idx(self) -> np.ndarray:
        """
        Return the idx of the first neighbor cell identified from the query, for
        each cell in the query.
        """
        return self._X_nn[:, 0].flatten()

    @property
    def _X_NN_0(self) -> np.ndarray:
        """
        Fetch the first neighbor cell from query, for each query cell.
        """
        return adata_query.fetch(
            self._adata[self._NN_0_idx],
            key=self._use_key,
            torch=False,
        )

    @property
    def _self_id(self) -> bool:
        """
        Answer whether all of the first cells identified from the nn query
        is that same as the input query.
        """
        return np.all(self._X_NN_0 == self._X_query)

    def check_self_id(
        self, X_query: np.ndarray, X_nn: np.ndarray, *args, **kwargs
    ) -> bool:
        
        """
        Parameters:
        -----------
        X_query: np.ndarray
        
        X_nn: np.ndarray
        
        Returns
        -------
        self_id: bool
        """
        
        self.__update__(locals())

        return self._self_id