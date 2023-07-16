#!/usr/bin/python3

"""The module has a function that deserializes an object to json"""
import json


def from_json_string(my_str):
    """Define a function that deserializes json to string
    Args:
        my_str (str): the string to use for json
    """

    result = json.loads(my_str)
    return result
