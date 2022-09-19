#!/usr/bin/python3
"""0-read-file module"""


def append_write(filename=None, text=None):
    """
    Reads a file without putting a lot of thought into it.
    """
    if filename and text is not None:
        with open(filename, mode="a", encoding="utf-8") as outfile:
            return outfile.write(text)
    return 0
