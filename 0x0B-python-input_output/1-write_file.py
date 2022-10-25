#!/usr/bin/python3

"""Defines a function that writes into a text file"""


def write_file(filename="", text=""):
    """Write a string to a text file

    Args:
        filename (str): The name of the file.
        text (str): the text to writte.
    Returns:
        The number of characters.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
