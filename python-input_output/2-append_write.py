#!/usr/bin/python3
""" Write a function that appends a string at the end of a text file (UTF8)
            and returns the number of characters added """

def append_write(filename="", text=""):
    """function that appends a string and returns the number of characters"""
    with open(filename, mode="w", encoding="UTF-8") as myfile:
        txt = myfile.write(text)
        return txt
