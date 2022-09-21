#!/usr/bin/python3
"""
3-to_json_string module
"""

# Standard Modules
import json
# My Modules
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file



def load_from_json_file(fp):
    """
    Returns JSON representation of object
    """
    if fp is not None:
        with open(fp, encoding="utf-8") as infile:
            return json.load(infile)
    return None
