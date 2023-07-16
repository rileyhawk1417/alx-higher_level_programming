#!/usr/bin/python3
"""The module just has a function that appends to a file"""


def append_write(filename="", text=""):
    """Define a function that appends to a file with given text
    Args:
        filename (str): the file to use
        text (str): the text to use in a string
    """
    with open(filename, "a") as file:
        print(file.write(text))
