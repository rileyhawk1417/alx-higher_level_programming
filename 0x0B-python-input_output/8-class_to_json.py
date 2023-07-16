#!/usr/bin/python3
"""Define a module that handles class to json"""


def class_to_json(obj):
    """Return dictionary structure of given data structures"""
    return obj.__dict__
