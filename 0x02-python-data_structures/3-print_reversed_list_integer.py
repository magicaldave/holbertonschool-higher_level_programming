#!/usr/bin/python3
"""Prints all items in a list"""


def print_reversed_list_integer(my_list=None):
    """Prints integers in a list"""
    if my_list is None:
        my_list = []
    for in_int in reversed(my_list):
        print("{:d}".format(in_int))
