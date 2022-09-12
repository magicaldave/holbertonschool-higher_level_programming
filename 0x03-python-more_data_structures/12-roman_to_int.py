#!/usr/bin/python3
"""Roman to Int Module"""


def roman_to_int(roman_string):
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
    for n in range(len(roman_string)):
        rchar = roman_string[n]
        if rchar == 'I' and n + 1 != len(roman_string) and roman_string[
                n + 1] != 'I':
            r_sum -= 1
        else:
            r_sum += roman_dict[roman_string[n]]
    return r_sum
