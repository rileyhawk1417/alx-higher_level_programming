#!/usr/bin/python3
"""Define a function that prints names"""


def say_my_name(first_name, last_name=""):
    """Print the name
    Args:
        first_name (str): First name
        last_name (str): Last name(surname)
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
