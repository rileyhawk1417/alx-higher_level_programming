#!/usr/bin/python3
"""Define a function that prints a square with '#'"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for idx in range(size):
        [print("#", end="") for row in range(size)]
        print("")
