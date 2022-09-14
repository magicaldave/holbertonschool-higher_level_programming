#!/usr/bin/python3
"""In-list Replacement Module"""


def replace_in_list(my_list, idx, element):
    """
    This function adds elements to a specific location in a list,
    Replacing the original values.
    """
    # check for valid index
    if idx >= 0 <= len(my_list):
        # add element at idx
        my_list.insert(idx, element)
        # remove at idx + 1
        del my_list[idx + 1]
    return my_list
