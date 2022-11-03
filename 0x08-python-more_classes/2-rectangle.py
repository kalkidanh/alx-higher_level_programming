#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """Representation of a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialze a new rectangle

        Args:
            width (int): The width of the new rectangle
            heignt (int): The heignt of the new rectangle
        """
        self.width = width
        self.heignt = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Getter for the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
