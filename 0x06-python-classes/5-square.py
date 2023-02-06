#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Represent the square."""

    def __init__(self, size=0):
        """Initialize the new square.

        Args:
            size (int): The size of the square"""

        self.__size = size

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """Print the square with # """
        if (self.size != 0):
            for i in range(self.size):
                print("#" * self.size)
        else:
            print()
