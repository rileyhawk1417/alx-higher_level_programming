#!/usr/bin/python3

"""Define a function that loads from a json file"""
import json


def load_from_json_file(filename):
    """function that reads from a json file
    Args:
        filename (str): File to use
    """
    with open(filename, "r") as file:
        return json.load(file)
