#!/usr/bin/python3

"""Define a lookup method for objects"""


def lookup(obj):
    """Looks up methods & attributes in object
    Though dir just returns everything it finds
    Args:
        obj (obj): object to look into
    """
    return dir((obj))
