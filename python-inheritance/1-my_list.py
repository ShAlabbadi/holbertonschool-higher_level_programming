#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """MyList class inherits from list and adds a print_sorted method."""
    def print_sorted(self):
        """Prints the list in ascending order
        without modifying the original list."""
        print(sorted(self))

    def str(self):
        """Returns the string representation of the list."""
        return str(list(self))
