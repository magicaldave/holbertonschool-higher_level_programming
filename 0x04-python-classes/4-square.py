#!/usr/bin/python3
"""0-Square Module"""


class Square:
    """Square Class!"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size**2

    def my_print(self):
        """Prints out the square provided"""
        for n in range(0, self.__size):
            print(self.__size * "#")

    @property
    def size(self):
        "Getter for private attr 'self'"
        return self.__size

    @size.setter
    def size(self, size):
        """Updates square size, if the input is valid."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
