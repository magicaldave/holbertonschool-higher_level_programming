#!/usr/bin/python3
"""In-list Replacement Module"""


def new_in_list(my_list, idx, element):
    """
    This function adds elements to a specific location in a list,
    Replacing the original values.
    """
    # Return a copy, regardless of valid input
    n_list = my_list[:]
    # check for valid index
    if 0 <= idx < len(my_list):
        # remove at idx
        del n_list[idx]
        # add element at idx
        n_list.insert(idx, element)
    return n_list
