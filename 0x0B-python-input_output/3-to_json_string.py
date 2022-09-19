#!/usr/bin/python3
"""

"""

import json


def to_json_string(my_obj):
    """
    Returns JSON representation of object
    """
    if my_obj is not None:
        return json.dumps(my_obj)
