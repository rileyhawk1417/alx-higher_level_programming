#!/usr/bin/python3
"""Determine if obj is an inheritance of class"""


def inherits_from(obj, a_class):
    """Check if the classes is an inheritance from another
    Args:
        obj (any): object given
        a_class (type): given type to match with
    Returns:
        If issubclass(type(obj), a_class) - true
        If !issubclass(type(obj), a_class) - false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
       return True
    return False
