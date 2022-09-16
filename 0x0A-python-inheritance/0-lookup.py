#!/usr/bin/python3
"""
0-Lookup Module
"""


def lookup(obj):
    """
    Returns a list containing all possible attributes and methods
    for a given object.
    """
    return dir(obj)
