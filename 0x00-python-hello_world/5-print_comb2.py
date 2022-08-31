#!/usr/bin/python3
"""Prints numbers up to 99, space-separated"""
i = 0
while i < 99:
    print("{:02d},".format(i), end=" ")
    i += 1
print(i)
