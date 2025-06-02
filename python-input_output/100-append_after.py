#!/usr/bin/python3
"""Module containing function that modifies file"""


def append_after(filename="", search_string="", new_string=""):
    """ a function that inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, 'r+') as f:
        lines = [line for line in f]
        f.seek(0)
        for idx, line in enumerate(lines):
            if search_string in line:
                lines.insert(idx + 1, new_string)
        f.writelines(lines)
