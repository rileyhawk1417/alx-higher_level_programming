#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Class meant to represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Init a new Rectangle.
        Args:
            width (int): The width of a new rectangle
            height (int): The height of a new rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width Property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
