#!/usr/bin/python3
"""  a class MyList that inherits from list """


class MyList(list):
    """ a class named MyList"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted(self))
        return sorted_list

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
