#!/usr/bin/python3
"""Defines a function that reads JSON."""
import json


def load_from_json_file(filename):
    """Create a python object fron a JSON file."""
    with open(filename) as f:
        return json.load(f)
