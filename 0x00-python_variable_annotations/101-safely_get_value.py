#!/usr/bin/env python3
"""Module for involved type annotations"""

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
mxd = Union[Any, T]
combd = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: combd = None) -> mxd:
    '''Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
