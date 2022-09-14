#!/usr/bin/python3
"""In-list Replacement Module"""


def replace_in_list(my_list, idx, element):
    """
    This function adds elements to a specific location in a list,
    Replacing the original values.
    """
    # check for valid index
    if 0 <= idx < len(my_list):
        # remove at idx
        del my_list[idx]
        # add element at idx
        my_list.insert(idx, element)
    return my_list
