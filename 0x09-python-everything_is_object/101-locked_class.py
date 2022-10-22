#!/usr/bin/python3
"""
Module for a class that prevents dynamic attribute creation

"""


class LockedClass():
    """Class to prevent dynamic attribute creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
