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
        workdict = self.__dict__.copy()
        if attrs is not None:
            workdict = {k: v for (k, v) in workdict.items() if k in attrs}
        return workdict

    def reload_from_json(self, json):
        """ Replaces all data in an input class"""
        for stat in json:
            self.__dict__[stat] = json[stat]
