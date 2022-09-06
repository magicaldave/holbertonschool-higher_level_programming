#!/usr/bin/python3
"""Square Matrix Module"""


def square_matrix_simple(matrix=None):
    """Takes a matrix input and returns the squares of each element"""
    return [[n ** 2 for n in row]for row in matrix]
