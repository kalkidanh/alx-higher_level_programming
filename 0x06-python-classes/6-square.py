#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Represent the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the new square.

        Args:
            size (int): The size of the square
            position (int, int): The position of the square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((type(value) != tuple) or (len(value) != 2)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if ((type(value[0]) != int) or (type(value[1]) != int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if ((value[0] < 0) or (value[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with # """
        if (self.size != 0):
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print((" " * self.position[0]) + ("#" * self.size))
        else:
            print()
