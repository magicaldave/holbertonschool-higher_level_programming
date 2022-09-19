#!/usr/bin/python3
"""
3-to_json_string module
"""

import json


def save_to_json_file(my_obj, fp):
    """
    Returns JSON representation of object
    """
    if my_obj is not None:
        with open(fp, mode="w", encoding="utf-8") as outfile:
            json.dump(my_obj, outfile)
