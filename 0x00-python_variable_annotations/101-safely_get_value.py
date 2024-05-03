#!/usr/bin/env python3
"""
    Defines 101-safely_get_value module
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
Def = Union[T, None]
retType = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> retType:
    """
        Retrieves a value from a dict using the given key
    """
    if key in dct:
        return dct[key]
    else:
        return default
