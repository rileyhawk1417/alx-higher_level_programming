#!/usr/bin/python3
"""The module just has a function that writes to a file"""


def write_file(filename="", text=""):
    """Define a function that writes to a file with given text
    Args:
        filename (str): The filename for the file
        text (str): the text to write in a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        print(file.write(text))
