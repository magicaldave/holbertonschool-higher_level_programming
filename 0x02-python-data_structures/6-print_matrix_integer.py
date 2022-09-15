#!/usr/bin/python3
"""Print Matrix Module"""


def print_matrix_integer(biglist=None):
    """Prints all elements of a matrix"""
    if biglist is not None:
        printed = 0
        for sublist in biglist:
            if printed == len(sublist):
                print("")
                printed = 0
            for number in sublist:
                print("{}".format(number), end=" ")
                printed += 1
    print("")
