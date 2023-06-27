#!/usr/bin/python3

"""
Define a class Square that handles validation
Which also has a public attribute
Class has getters & setters
"""


class Square:
    """
    Square class with private instance attribute
    The method validates if the @size is a int & is greater than 0
    There are getters & setters
    """

    def __init__(self, size=0):
        """
        Init a new square.
        Args:
            size (int): The size of a new square
        """
        self.size = size

    @property
    def size(self):
        """A property that returns that can set/get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter that sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The function returns the area of size"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character"""
        for items in range(0, self.__size):
            [print("#", end="") for item in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
