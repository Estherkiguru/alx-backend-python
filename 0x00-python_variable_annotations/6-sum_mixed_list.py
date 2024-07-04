#!/usr/bin/env python3
"""Module for type-annotated function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list mxd_lst of integers and floats
    returns:sum as float
    """
    return sum(mxd_lst)
