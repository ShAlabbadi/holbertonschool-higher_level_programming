#!/usr/bin/python3
"""Define an empty class named BaseGeometry"""


class BaseGeometry:
    """The BaseGeometry class"""
    def area(self):
        """A method that raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A method that validaties a value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
