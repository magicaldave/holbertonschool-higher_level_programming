#!/usr/bin/python3
"""Search & Replace Module"""


def search_replace(my_list, search, replace):
    """Find Search in My_List and Overwrite with Replace"""
    n_list = list.copy(my_list)
    if n_list.count(search) > 0:
        for n in n_list:
            if n == search:
                i = n_list.index(n)
                n_list.remove(n)
                n_list.insert(i, replace)

    return n_list
