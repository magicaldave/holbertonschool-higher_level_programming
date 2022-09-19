#!/usr/bin/python3
"""
3-to_json_string module
"""

import json


def from_json_string(my_obj):
    """
    Returns JSON representation of object
    """
    if my_obj is not None:
        return json.dumps(my_obj)
    return None
