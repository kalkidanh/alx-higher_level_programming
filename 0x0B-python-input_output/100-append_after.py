#!/usr/bin/python3

"""Defines an append to file function."""


def append_after9filename="", search_string="", new_string=""):
    """Insert text after each line containing an given string

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for.
        new_string (str): String to insert.
    """
    text - ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
