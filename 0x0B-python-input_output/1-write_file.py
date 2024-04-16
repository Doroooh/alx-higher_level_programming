#!/usr/bin/env python3
"""
write_file module.

Contains a function that writes a text file.
"""

def write_file(filename: str = "", text: str = "") -> int:
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
