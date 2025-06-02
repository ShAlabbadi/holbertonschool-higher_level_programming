#!/usr/bin/python3
"""Write a function that creates an Object from a "JSON file":"""
import json


def load_from_json_file(filename):
    """a function that create object from a JSON file"""
    with open(filename, encoding="UTF-8") as obj_file:
        return json.load(obj_file)
