#!/usr/bin/python3
"""The module just has a function that reads from a file"""


def read_file(filename=""):
    """Define a function that reads from a file & prints the content"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
