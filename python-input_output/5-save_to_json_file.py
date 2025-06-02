#!/usr/bin/python3
"""Write a function that writes an Object to a text file(using a JSON)"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file"""
    with open(filename, mode="w", encoding="UTF-8") as myfile:
        text = myfile.write(json.dumps(my_obj))
        return text
