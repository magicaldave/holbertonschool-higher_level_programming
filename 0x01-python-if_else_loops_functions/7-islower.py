#!/usr/bin/python3
"""Islower module"""


def islower(c):
    """Checks if provided char is a lowercase letter"""
    if ord(c) < 123 and ord(c) > 96:
        return True
    return False
