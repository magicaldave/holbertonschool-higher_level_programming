#!/usr/bin/python3
"""Uppercase Module"""


def uppercase(str):
    """Prints string in uppercase"""
    g = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            x = ord(ch) - 32
        else:
            x = ord(ch)
        y = chr(x)
        g = g + y
    print(g)
