#!/usr/bin/python3
"""Define a function to find the max integer in a list"""


def max_integer(list=[]):
    """Find the max integer in a list if list is empty return None"""
    if len(list) == 0:
        return None
    result = list[0]
    idx = 1
    while idx < len(list):
        if list[idx] > result:
            result = list[idx]
        idx += 1
    return result
