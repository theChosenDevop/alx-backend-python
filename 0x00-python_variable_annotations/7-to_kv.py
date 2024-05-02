#!/usr/bin/env python3
"""
    Defines 7-to_kv module
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Returns tuple of k and square of v
    """
    return (k, v * v)
