#!/usr/bin/python3
"""Write a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """function that returns an obj represented by a JSON"""
    return json.loads(my_str)
