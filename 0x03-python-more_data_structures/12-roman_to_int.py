#!/usr/bin/python3
"""Roman to Int Module"""


def roman_to_int(r_str):
    """
    Translates Roman numerals into integers based on a dictionary.
    @roman_string: roman numerals to translate as string.
    """
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    r_sum = 0
    prev = None
    if isinstance(r_str, str):
        # Roman numerals are read backwards, so we exploit Python and skip 0
        for n in range(1, len(r_str) + 1):
            # Capture the current character by its dict value
            # Before I wrapped it in roman_dict[], I was only
            # Comparing characters and kept getting unexplainable results!
            # By definition, the ASCII value for L is less than X,
            # But the opposite is true in roman numerals.
            current = roman_dict[r_str[-n]]
            # Skip comparing values if there isn't one to compare
            if prev and current < prev:
                r_sum -= current
            else:
                r_sum += current

            # Store it for comparison on later iterations
            prev = current
    return r_sum
