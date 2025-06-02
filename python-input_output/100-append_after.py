#!/usr/bin/python3
"""Module containing function that modifies file"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(new_lines)
