#!/usr/bin/python3
"""
Student Class Module - 9 version
"""


class Student:
    """ Student class for 9-student """

    def __init__(self, f_name, l_name, age):
        """ Initializer for Student class"""
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dict representation like 8-class_to_json """
        if attrs is not None:
            return {k: v for (k, v) in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all data in an input class"""
        for stat in json:
            self.__dict__[stat] = json[stat]
