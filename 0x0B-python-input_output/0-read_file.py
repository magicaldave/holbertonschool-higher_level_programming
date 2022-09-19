#!/usr/bin/python3
"""0-read-file module"""


def read_file(filename=None):
    """
    Reads a file without putting a lot of thought into it.
    """
    if filename is not None:
        with open(filename, encoding="utf-8") as outfile:
            print(outfile.read(), end="")
