#!/usr/bin/python3
"""A class that defines a square with size validation and area calculation"""



class Square:
    """ defines class named Square """

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """property to retrieve the size"""
        return self.__size    

    @size.setter
    def size(self, value):
        """property setter to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method returns the current square area"""
        return self.__size * self.__size
