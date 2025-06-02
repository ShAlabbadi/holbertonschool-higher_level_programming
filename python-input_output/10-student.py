#!/usr/bin/python3
"""Write a class Student that defines a student by: (based on 9-student.py)
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

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary of a Student instance"""
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[elements], str) for elements in attrs):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}
