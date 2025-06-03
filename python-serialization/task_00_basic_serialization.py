#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file to a Python dictionary.
    
    Args:
        filename: The filename of the input JSON file
        
    Returns:
        A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r') as f:
        return json.load(f)
