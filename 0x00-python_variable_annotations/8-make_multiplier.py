#!/usr/bin/env python3
"""Module for type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument
    returns: function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
