#!/usr/bin/python3
"""Print and return last digit"""


def print_last_digit(num):
    """Print last digit of input (num)"""
    n_num = abs(num) % 10
    print(n_num, end="")
    return n_num
