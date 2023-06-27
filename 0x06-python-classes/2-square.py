#!/usr/bin/python3

"""Define a class Square that handles validation"""


class Square:
    """
    Square class with private instance attribute
    The method validates if the @size is a int & is greater than 0
    """

    def __init__(self, size=0):
        """
        Init a new square.
        Args:
            size (int): The size of a new square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
