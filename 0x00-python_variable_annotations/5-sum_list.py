#!/usr/bin/env python3
"""Module for type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats as argument
    returns: sum as float
    """
    return sum(input_list)
