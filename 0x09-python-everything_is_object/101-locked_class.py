#!/usr/bin/python3
"""LockedClass module."""


class LockedClass:
    """LockedClass class containing only __slots__."""
    __slots__ = ['first_name']

    def __init__(self, first_name):
        self.first_name = first_name
