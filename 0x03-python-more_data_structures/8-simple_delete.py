#!/usr/bin/python3
"""Dict Delete Module"""


def simple_delete(a_dictionary, key=""):
    """Deletes an element from a_dictionary"""
    try:
        del a_dictionary[key]
    except KeyError:
        pass
    return a_dictionary
