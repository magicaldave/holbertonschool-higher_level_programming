#!/usr/bin/python3
"""
Sorted list class module
"""


class MyList(list):
    """This class defines a -special- list"""

    def print_sorted(self):
        """Prints itself, in numerical order"""
        print(sorted(self))
