#!/usr/bin/env python3
"""
Student module.

Contains a Student class and some methods.
"""


class Student:
    """Defines a Student."""

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Initializes a Student object with provided attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self) -> dict:
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the attributes of the Student.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
