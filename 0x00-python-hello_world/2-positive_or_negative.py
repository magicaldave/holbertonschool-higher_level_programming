#!/usr/bin/python3
"""Gets a random integer and determines its signedness"""
import random

number = random.randint(-10, 10)
i = 0
signedness = ["zero", "negative", "positive"]
if number < 0:
    i = 1
elif number > 0:
    i = 2

print('{} is {}'.format(number, signedness[i]))
