#!/usr/bin/python3
"""Rectangle Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class for rectangle that inherits base geometry"""

    def __init__(self, width, height):
        """Init a new rectangle
        Args:
            width (int): the given width of rectangle
            height (int): the given height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

