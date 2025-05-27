#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance of
the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """check is the 'obj' the same as the 'a_class'"""
    return type(obj) is a_class
