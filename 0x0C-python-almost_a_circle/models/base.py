#!/usr/bin/python3
"""
Base module for "Almost a Circle"
"""


class Base:
    """
    Base Class to inherit
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializer for Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def hw_check(self, val, name):
        """
        Checks if the input is a valid int
        """
        if type(val) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if val <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        return val

    def xy_check(self, val, name):
        """
        Checks if the input is a valid int
        """
        if type(val) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if val < 0:
            raise ValueError("{:s} must be >= 0".format(name))
        return val
