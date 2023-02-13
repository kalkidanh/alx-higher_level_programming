#!/usr/bin/python3
"""Base class module"""

class Base:
    """Initialize Base class"""
    __nb_objects = 0

    def __init__(self, id=none):
        """Initialize instance from base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
