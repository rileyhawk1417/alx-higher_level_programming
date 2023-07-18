#!/usr/bin/python3
"""Determine if obj is same type of class"""


def is_same_class(obj, a_class):
    """Check if the classes are the same by type
    Args:
        obj (any): object given
        a_class (type): given type to match with
    Returns:
        If obj == to a_class - true
        If obj != to a_class - false
    """
    if type(obj) == a_class:
        return True
    return False
