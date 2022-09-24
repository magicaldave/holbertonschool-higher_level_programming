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
        self.__width = self.int_check(width, "width")
        self.__height = self.int_check(height, "height")
        self.__x = self.int_check(x, "x")
        self.__y = self.int_check(y, "y")
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        self.__width = self.int_check(value, "width")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = self.int_check(value, "height")

    @property
    def x(self):
        """Getter for height"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for height"""
        self.__x = self.int_check(value, "x")

    @property
    def y(self):
        """Getter for height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for height"""
        self.__y = self.int_check(value, "y")

    def area(self):
        """returns square area"""
        return self.__height * self.__width

    def display(self):
        """
        Prints out the rectangle you made!
        """
        print(self.__y * "\n",
              (self.__x * " " + "#" * self.__width + "\n") * self.__height,
              sep="",
              end="")
