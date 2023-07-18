#!/usr/bin/python3
"""Define a class for geometry"""

class BaseGeometry:
    """Base class for geometry with methods"""
    def area(self):
       """Function not implemented""" 
       raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
       """Validate value as integer
       Args:
           name (str): name of parameter being passed
           value (int): the integer itself
       Raises:
           TypeError: if value is not an integer
           ValueError: if value is <= 0
       """
       if type(value) != int:
            raise TypeError("{} must be an integer".format(name)) 
       if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
