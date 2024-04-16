#!/usr/bin/env python3
"""
write_file module.

Contains a function that inserts a line of text into a file.
"""


def append_after(filename: str = "", search_string: str = "", new_string: str = "") -> None:
    """
    Inserts a line of text into a file after each occurrence
    of a specific string within each line.

    Args:
        filename (str): The path to the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing the search string.
    """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
