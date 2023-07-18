#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Method brings back a sorted list"""
        print(sorted(self))
