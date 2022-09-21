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

    def to_json(self):
        """ Returns dict representation like 8-class_to_json """
        return self.__dict__
