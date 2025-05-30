#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, n):
        """Equal"""
        if (self.real == n):
            return False
        return True

    def __noeq__(self, n):
        """Not equal"""
        if (self.real != n):
            return False
        return True
