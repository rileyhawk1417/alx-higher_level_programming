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

    def __init__(self, size=0, position=(0, 0)):
        """
        Init a new square.
        Args:
            size (int): The size of a new square
            position (int, int): Position of the square in tuple format
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """A property that returns that can set/get the size"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter that sets the square position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """The function returns the area of size"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character"""
        if self.__size == 0:
            print("")
            return

        [print("", end="") for item in range(self.__position[1])]
        for items in range(0, self.__size):
            [print(" ", end="") for item in range(self.__position[0])]
            [print("#", end="") for item in range(self.__size)]
            print("")
