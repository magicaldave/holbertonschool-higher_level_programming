#!/usr/bin/python3
""""""


def divisible_by_2(my_list=None):
    """"""
    r_list = []
    if my_list == []:
        return None
    if my_list is not None:
        for n in my_list:
            r_list += [not bool(n % 2)]
    return r_list
