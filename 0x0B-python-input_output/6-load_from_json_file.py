#!/usr/bin/python3
"""save_to_json_file module.
this contains a function to create an Object from the “JSON file”.
"""
import json


def load_from_json_file(filename):
    """Creating an Object from a “JSON file”."""
    with open(filename, 'r') as f:
        return json.load(f)
