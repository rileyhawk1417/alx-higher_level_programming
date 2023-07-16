#!/usr/bin/python3

"""
Define a class Student that has student attributes
Which also has a public attribute
Class has getters & setters
"""


class Student:
    """
    Student class with public attributes
    """

    def __init__(self, first_name, last_name, age):
        """Init a new student
        Args:
            first_name (str): First name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return student in dictionary format"""
        return self.__dict__
