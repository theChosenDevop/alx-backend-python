#!/usr/bin/env python3
"""
    Defines 6-sum_mixed_list module
"""

from typing import List,Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        returns the sum of int and float value
    """
    total = 0.0

    for num in mxd_lst:
        total += num
    return total
