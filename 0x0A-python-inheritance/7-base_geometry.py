#!/usr/bin/python3
"""Define a BaseGeometry class"""


class BaseGeometry:
    """Represent a base geometry class"""

    def area(self):
        """a function raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validates a parameter value be positive integer or not

        Args:
            name: name of parameter
            value: the parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
