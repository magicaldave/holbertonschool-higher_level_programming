#!/usr/bin/python3
"""Print alphabet, minus a newline"""
i = 97
while i < 123:
    print("{0:c}".format(i), end="")
    i += 1
