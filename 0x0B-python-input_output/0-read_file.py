#!/usr/bin/python3
"""The module just has a function that reads from a file"""


def read_file(filename=""):
    """Define a function that reads from a file & prints the content"""
    with open(filename, "r") as file:
        print(file.read())
