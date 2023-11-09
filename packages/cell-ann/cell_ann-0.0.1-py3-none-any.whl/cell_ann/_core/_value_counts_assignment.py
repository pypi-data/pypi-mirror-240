
import ABCParse
import pandas as pd
import numpy as np

from typing import Union


class ValueCountAssignment(ABCParse.ABCParse):
    def __init__(self, *args, **kwargs):
        self.__parse__(locals())

    def forward(self):
        return (
            pd.DataFrame(self._neighbor_vals.squeeze(-1))
            .apply(pd.Series.value_counts, axis=1)
            .fillna(0)
        )

    def max_assign(self, value_counts):
        return value_counts.idxmax(1).values

    def __call__(
        self, neighbor_vals: np.ndarray, max_only: bool = True, *args, **kwargs
    ):
        self.__update__(locals())

        value_counts = self.forward()
        if max_only:
            return self.max_assign(value_counts)
        return value_counts


def count_based_assignment(
    neighbor_vals: np.ndarray, max_only: bool = True, *args, **kwargs
) -> Union[np.ndarray, pd.DataFrame]:
    """

    Parameters
    ----------
    neighbor_vals: np.ndarray

    max_only: bool, default = True

    Returns
    -------
    consensus_assignment: np.ndarray or value_counts: pd.DataFrame
    """
    value_count_assignment = ValueCountAssignment()
    return value_count_assignment(neighbor_vals=neighbor_vals, max_only=max_only)

class CountBasedAssignmentMixIn(object):
    def count_based_assignment(self, neighbor_vals: np.ndarray, max_only: bool = True):
        return count_based_assignment(neighbor_vals=neighbor_vals, max_only=max_only)
