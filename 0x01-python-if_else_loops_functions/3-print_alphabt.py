#!/usr/bin/python3
"""Prints alphabet, minus q and e"""
i = 97
while i < 123:
    if i not in (113, 101):
        print('{:c}'.format(i), end="")
    i += 1
