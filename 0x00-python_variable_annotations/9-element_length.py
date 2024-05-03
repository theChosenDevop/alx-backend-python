#!/usr/bin/env python3
"""
    Defines 9-element_length module
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Returns the length of sequence
    """
    return [(i, len(i)) for i in lst]
