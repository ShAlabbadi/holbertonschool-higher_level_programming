#!/usr/bin/python3
"""Define an empty class named BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        BaseGeometry.integer_validator(self, 'width', height)
        self.__width = width
        BaseGeometry.integer_validator(self,'height', width)
        self.__height = height
