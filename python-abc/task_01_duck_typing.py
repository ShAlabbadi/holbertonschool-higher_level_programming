#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi



class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """return area of shapes"""
        pass

    @abstractmethod
    def perimeter(self):
        """return perimeter of shapes"""
        pass


class Circle(Shape):
    """Circle implementation of Shape"""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """return perimeter of Circle"""
        return pi * self.radius**2

    def perimeter(self):
        """return perimeter of Circle"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation of Shape"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """return area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter of Rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of any shape-like object"""
#    area = shape.area()
 #   perimeter = shape.perimeter()
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
