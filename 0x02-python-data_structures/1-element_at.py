#!/usr/bin/python3
"""C-like element fetching module"""


def element_at(my_list, idx):
    """Returns idx of my_list"""
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]
