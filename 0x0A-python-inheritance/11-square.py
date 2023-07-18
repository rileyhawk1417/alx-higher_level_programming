#!/usr/bin/python3

"""Square Class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class for square that inherits Rectangle"""

    def __init__(self, size):
        """Init a new Square
        Args:
            size (int): the size for the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
