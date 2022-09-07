#!/usr/bin/python3
"""Doubles key values in dictionary"""


def multiply_by_2(a_dictionary):
    """Returns dict with doubled values"""
    return {k: v * 2 for k, v in a_dictionary.items()}
