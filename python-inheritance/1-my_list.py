#!/usr/bin/python3
"""  a class MyList that inherits from list """


class MyList(list):
    """ a class named MyList"""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))

#if __name__ == "__main__":
    #import doctest
    #doctest.testfile("tests/1-my_list.txt")
