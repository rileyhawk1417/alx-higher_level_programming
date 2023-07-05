#!/usr/bin/python3

""" Defines function - add_integer
    Raises:
        TypeError: if a or b is not in or float
"""


def add_integer(a, b=98):
    """Returns the sum of a + b
    >>> add_integer(2, 98)
    100
    >>> add_ineteger(15.45, 'f')
    fail
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
