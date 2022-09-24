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

    def int_check(self, val, name):
        """
        Checks if the input is a valid int
        """
        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer")
        if (val <= 0 and name not in ('x', 'y')) or val < 0:
            raise ValueError(
                f"{name} must be {'>=' if name in ('x', 'y') else '>'} 0")
        return val
