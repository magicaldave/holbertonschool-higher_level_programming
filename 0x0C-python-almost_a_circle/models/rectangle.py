#!/usr/bin/python3
"""
Rectangle Class module
"""

from models.base import Base


class Rectangle(Base):
    """
    Inherits unique id from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        You have to input measurements for the
        rectangle in order to make one.
        """
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if isinstance(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if isinstance(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for height"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for height"""
        if isinstance(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__x = value

    @property
    def y(self):
        """Getter for height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for height"""
        if isinstance(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__y = value
