#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """ a class named Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = []
            for i in range(self.__height):
                rectangle_str.append(str(self.print_symbol) * self.__width)
            return "\n".join(rectangle_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
    
        area_1 = rect_1.area()
        area_2 = rect_2.area()
    
        return rect_1 if area_1 >= area_2 else rect_2
