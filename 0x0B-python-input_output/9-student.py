#!/usr/bin/python3

"""Define thr class Student."""

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """initialize a new student.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the student."""
        return self.__dict__
