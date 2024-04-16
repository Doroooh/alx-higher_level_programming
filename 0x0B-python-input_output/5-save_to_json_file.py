#!/usr/bin/python3
"""save_to_json_file module.
this will contain a function to write an Object to text files.
"""
import json

def save_to_json_file(my_obj, filename):
    """Writing the object to text files using the JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
