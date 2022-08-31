#!/usr/bin/python3
"""Prints unique combinations of two numbers"""
y = 1
for x in range(0, 80, 10):
    for y in range(1, 10):
        if y > x / 10:
            print("{:02d},".format(x + y), end=" ")
    y = 1
print("89")
