#!/usr/bin/python3

"""Define a function that checks a class for instances of it."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class.

    Args:
        obj (any): Object to be checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        If object is exactly an instance of a_class True.
        Otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
