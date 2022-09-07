#!/usr/bin/python3
"""Sorted Dict Module"""


def print_sorted_dictionary(a_dictionary):
    """Prints alphabetically sorted"""
    for i, j in sorted(dict.items(a_dictionary)):
        print("{}: {}".format(i, j))
