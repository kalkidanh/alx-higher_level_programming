#!/usr/bin/python3

"""Defines a class named BaseGeometry."""


class BaseGeometry:
    """Represents the class base geometry."""
    
    def area(self):
        """Raises an exception when area is not implemented."""
        raise Exception("area() is not implemented")
