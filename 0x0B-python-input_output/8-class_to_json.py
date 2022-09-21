#!/usr/bin/python3
"""
Returns class as json-ready dictionary
"""


def class_to_json(obj):

    # Turns out, there's a dict method that does this work for me.
    return (obj.__dict__)
