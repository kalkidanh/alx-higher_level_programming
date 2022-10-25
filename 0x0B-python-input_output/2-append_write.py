#!/usr/bin/python3

"""Defines a function that appends into a text file"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file

    Args:
        filename (str): The name of the file.
        text (str): the text to writte.
    Returns:
        The number of characters.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
