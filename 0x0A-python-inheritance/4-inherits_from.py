#!/usr/bin/python3
"""
This module uses the isinstance() function.
"""


def inherits_from(obj, in_class):
    """
    This function checks if a given object matches a provided class.
    """
    if isinstance(obj, in_class) and type(obj) is not in_class:
        return True
    return False
