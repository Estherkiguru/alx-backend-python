#!/usr/bin/env python3
"""Module for type-annotated function to_kv"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments
    returns: Tuple
    first element: string
    second element: square of the int/float v
    """
    return (k, float(v ** 2))
