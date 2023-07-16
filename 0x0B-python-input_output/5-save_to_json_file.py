#!/usr/bin/python3

"""Define a function that saves to a file in json format"""
import json


def save_to_json_file(my_obj, filename):
    """function that saves to a file in json format
    Args:
        my_obj (obj): object to use
        filename (str): filename to use
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
