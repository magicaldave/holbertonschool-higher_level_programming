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
        self.__width = self.hw_check(width, "width")
        self.__height = self.hw_check(height, "height")
        self.__x = self.xy_check(x, "x")
        self.__y = self.xy_check(y, "y")
        super().__init__(id)

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        self.__width = self.hw_check(value, "height")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = self.hw_check(value, "height")

    @property
    def x(self):
        """Getter for height"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for height"""
        self.__x = self.xy_check(value, "x")

    @property
    def y(self):
        """Getter for height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for height"""
        self.__y = self.xy_check(value, "y")
