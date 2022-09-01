#!/usr/bin/python3
"""Safe division of integers"""


def safe_print_division(a, b):
    """Executes and prints division result"""
    div = ""
    try:
        div = a / b
    except ZeroDivisionError:
        div = "None"
    finally:
        print("Inside result: {0}".format(div))
        return div
