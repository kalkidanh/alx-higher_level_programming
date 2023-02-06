#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """Represent a class named base geometry"""

    def area(self):
        """a function raises an Exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates if an input is of int type.

        Args:
            name (str): Name of parameter.
            value (int): Parameter to validate.
        Raises:
            TypeError: Value is not an int type.
            ValueError: Value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
