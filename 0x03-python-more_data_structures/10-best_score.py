#!/usr/bin/python3
"""Dict Scoring Module"""


def best_score(a_dictionary):
    """Uses max() to find biggest value in a dict"""
    if a_dictionary:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
    return None
