#!/usr/bin/python3

"""Defines a function that checks an inherited class ."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is an inherited instance of a class True.
        Otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
