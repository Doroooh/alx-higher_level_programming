#!/usr/bin/python3
"""from_json_string module.
it contains a function that returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    this will return an object like in Python data structure represented by a JSON string:.
    """
    return json.loads(my_str)
