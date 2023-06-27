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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The function returns the area of size"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define == (equal) operator to the square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define != (not equal) operator to the square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define < (less than) operator to the square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define <= (less than | equal to) operator to the square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define > (not equal) operator to the square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define >= (greater than | equal to) operator to the square"""
        return self.area() >= other.area()
