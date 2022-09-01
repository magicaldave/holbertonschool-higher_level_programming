#!/usr/bin/python3
"""Counts and prints all provided arguments"""
import sys
if __name__ == '__main__':
    ac = len(sys.argv)

    if ac == 1:
        print("0 arguments")
    else:
        i = 1
        if (ac - 1) == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(ac - 1))
        for i in range(1, ac):
            print("{}: {}".format(i, str(sys.argv[i])))
            i += 1
