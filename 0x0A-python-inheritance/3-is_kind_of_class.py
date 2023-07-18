#!/usr/bin/python3
"""Determine if obj is an instance of class"""


def is_kind_of_class(obj, a_class):
    """Check if the classes are the same by isinstance
    Args:
        obj (any): object given
        a_class (type): given type to match with
    Returns:
        If isinstance(obj, a_class) - true
        If !isinstance(obj, a_class) - false
    """
    if isinstance(obj, a_class):
        return True
    return False
