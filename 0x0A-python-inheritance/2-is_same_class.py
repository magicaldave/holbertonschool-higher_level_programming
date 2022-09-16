#!/usr/bin/python3
"""
This module uses the isinstance() function.
"""


def is_same_class(obj, in_class):
    """
    This function checks if a given object matches a provided class.
    """
    if type(obj) is in_class:
        return True
    return False
