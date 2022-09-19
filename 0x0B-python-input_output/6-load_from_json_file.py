#!/usr/bin/python3
"""
3-to_json_string module
"""

import json


def load_from_json_file(fp):
    """
    Returns JSON representation of object
    """
    if fp is not None:
        with open(fp, encoding="utf-8") as infile:
            return json.load(infile)
    return None
