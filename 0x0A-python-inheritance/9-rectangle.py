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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Simply return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print & str for the rectangle"""
        c_name = "[{}]".format(str(self.__class__.__name__)) 
        result = "{} {}/{}".format(c_name, str(self.__width), str(self.__height))
        return result
