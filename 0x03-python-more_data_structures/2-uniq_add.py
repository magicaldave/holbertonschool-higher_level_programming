#!/usr/bin/python3
"""Unique-Add Module"""


def uniq_add(my_list=None):
    """Adds together only unique elements of a list"""
    if my_list is None:
        my_list = []
    uniq_sum = 0
    for n in set(my_list):
        uniq_sum += n
    return uniq_sum
