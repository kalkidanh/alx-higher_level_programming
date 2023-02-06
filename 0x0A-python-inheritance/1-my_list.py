#!/usr/bin/python3

"""Defines a class MyList inherited from a base class."""


class MyList(list):
    """Applies sorting to the base class list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
