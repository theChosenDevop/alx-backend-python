#!/usr/bin/env python3
"""
    Defines 5-sum_list module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        returns sum of input_list as float
    """
    total = 0
    for num in input_list:
        total += num
    return total
