#!/usr/bin/python3
"""
Module containing class Shape and subclasses Circle and Rectangle.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    A class to define a shape.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    A class to define a circle.
    """
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return pi * self.__radius * self.__radius

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    A class to define a rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height


def shape_info(obj):
    area = obj.area()
    perimeter = obj.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
