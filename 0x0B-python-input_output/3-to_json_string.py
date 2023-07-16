#!/usr/bin/python3

"""The module has a function that serializes an object to json"""
import json


def to_json_string(my_obj):
    """Define a function that serializes a object to json
    Args:
        my_obj (obj): object to use
    """
    result = json.dumps(my_obj)
    return result
