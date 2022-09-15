#!/usr/bin/python3
"""Sorts a copy of a list to find its biggest integer"""


def max_integer(my_list=None):
    """Returns the largest value in a list"""
    if my_list == []:
        my_list = None
    if my_list is not None:
        my_list = sorted(my_list)[len(my_list) - 1]
    return my_list
