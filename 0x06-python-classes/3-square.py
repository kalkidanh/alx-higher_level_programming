#!/usr/bin/python3
"""class Square to define a square"""



class Square():
    """square class with size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
