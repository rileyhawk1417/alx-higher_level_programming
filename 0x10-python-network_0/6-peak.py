#!/usr/bin/python3
"""
Find the highest number in the array
"""


def find_peak(list_of_integers):
    """
    Find the highest number in a reversed array
    """
    if bool(list_of_integers) is False:
        return None

    list_of_integers.reverse()
    return list_of_integers[0]
