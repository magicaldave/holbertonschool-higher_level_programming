#!/usr/bin/python3
"""
Rectangle Class module
"""

from models.base import Base, int_check


class Rectangle(Base):
    """
    Inherits unique id from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        You have to input measurements for the
        rectangle in order to make one.
        """
        super().__init__(id)
        self.__width = int_check(width, "width")
        self.__height = int_check(height, "height")
        self.__x = int_check(x, "x")
        self.__y = int_check(y, "y")

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        self.__height = int_check(value, "height")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = int_check(value, "height")

    @property
    def x(self):
        """Getter for height"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for height"""
        self.__height = int_check(value, "x")

    @property
    def y(self):
        """Getter for height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for height"""
        self.__height = int_check(value, "y")
