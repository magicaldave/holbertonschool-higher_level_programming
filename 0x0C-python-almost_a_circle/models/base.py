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
            self.__nb_objects += 1
            self.id = self.__nb_objects
