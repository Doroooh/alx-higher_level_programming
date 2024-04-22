#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv
import os
import random
import turtle
import time

class Base:
    """A representation of the base of our OOP hierarchy."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """Jsonifies a dictionary."""
        if list_dicts is None or not list_dicts:
            return "[]"
        return dumps(list_dicts)

    @staticmethod
    def from_json_string(json_str):
        """Unjsonifies a dictionary."""
        if json_str is None or not json_str:
            return []
        return loads(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves jsonified object to file."""
        if list_objs is not None:
            list_dicts = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Loads string from file and unjsonifies."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """Loads instance from dictionary."""
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object to csv file."""
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open(f'{cls.__name__}.csv', 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
