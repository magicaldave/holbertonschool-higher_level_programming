#!/usr/bin/python3
"""
This module uses the isinstance() function.
"""


def is_kind_of_class(obj, in_class):
    """
    This function checks if a given object matches a provided class.
    """
    if isinstance(obj, in_class):
        return True
    return False
