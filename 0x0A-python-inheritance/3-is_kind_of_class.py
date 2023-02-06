#!/usr/bin/python3

"""Defines a class and inherited class function to check."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): The class that matches the type of object to.
    Returns:
        If object is an instance or inherited instance of a_class True.
        Otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
