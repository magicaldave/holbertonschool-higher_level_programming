#!/usr/bin/python3
"""Fizzbuzz Module"""


def fizzbuzz():
    """Classic Fizzbuzz Test in Python!"""
    spc = chr(32)
    for i in range(1, 101):
        if i % 5 and i % 3:  # Check first if none of the following apply
            print(i, end=spc)
        elif not i % 3 and i % 5:  # Divisible by 3 only
            print("Fizz", end=spc)
        elif not i % 5 and i % 3:  # Divisible by 5 only
            print("Buzz", end=spc)
        else:  # Divisible by both
            print("Fizzbuzz", end=spc)
