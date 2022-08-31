#!/usr/bin/python3
"""Gets random numbers and evaluates the last digit"""
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
i = 0
lastdig = (abs(number) % 10)  # Capture the last digit
suff = ["and is 0", "and is greater than 5", "and is less than 6 and not 0"]
if number < 0:
    lastdig = -lastdig  # Negate the number if necessary
if lastdig != 0:
    if lastdig > 5:
        i = 1
    else:
        i = 2
print("Last digit of {} is {} {}".format(number, lastdig, suff[i]))
