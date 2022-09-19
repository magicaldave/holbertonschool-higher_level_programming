#!/usr/bin/python3
"""0-read-file module"""


def write_file(filename=None, text=None):
    """
    Reads a file without putting a lot of thought into it.
    """
    if filename and text is not None:
        with open(filename, mode="w", encoding="utf-8") as outfile:
            return outfile.write(text)
    return 0
