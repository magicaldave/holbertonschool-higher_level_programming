#!/usr/bin/python3
"""Multiple Returns Module"""


def multiple_returns(sentence=None):
    """
    Returns a tuple of a sentence and its first character
    """
    if sentence == "":
        sentence = None
    if sentence is not None:
        return (len(sentence), sentence[0])
    return (0, None)
