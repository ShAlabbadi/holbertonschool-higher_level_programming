#!/usr/bin/python3
"""Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """Check if the class obj is a subclass of a_class"""
    return issubclass(type(obj), a_class)
