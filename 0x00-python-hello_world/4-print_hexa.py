#!/usr/bin/python3
"""Prints numbers up to 98 in hex and dec"""
i = 0
while i < 99:
    print("{0:d} = 0x{0:x}".format(i))
    i += 1
