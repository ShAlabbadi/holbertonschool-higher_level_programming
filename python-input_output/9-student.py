#!/usr/bin/python3
"""Write a class Student that defines a student by:
Public instance attributes:
1- first_name
2- last_name
3- age"""


class Student:
    """A class named 'Student'"""

    def __init__(self, first_name, last_name, age):
        """Initialize the class objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method def that retrieves a dictionary of a Student info"""
        return self.__dict__
