#!/usr/bin/python3

"""Defines a function tht writes an object to a file in JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """writes an object using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
