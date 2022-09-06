#!/usr/bin/python3
"""Search & Replace Module"""


def search_replace(my_list, search, replace):
    """Find Search in My_List and Overwrite with Replace"""
    return [n if n != search else replace for n in my_list]
