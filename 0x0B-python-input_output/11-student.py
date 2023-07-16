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

    def to_json(self, attrs=None):
        """Return student in dictionary format
        Display the elements that only have strings
        Args:
            attrs: (list): list of attributes to show
        """
        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload from json & replace all the attributes from the student
        Args:
            json (dict): key/value pairs to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
