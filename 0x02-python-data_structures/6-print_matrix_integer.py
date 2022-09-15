#!/usr/bin/python3
"""Print Matrix Module"""


def print_matrix_integer(biglist=[[]]):
    """Prints all elements of a matrix"""
    if biglist == [[]]:
        biglist = None

    if biglist is not None:
        printed = 0

        # Break the main list into sub-lists
        for sublist in biglist:
            if printed == len(sublist):
                print("")
                printed = 0

            # Act on each element of the sublist
            for number in sublist:
                print("{:d}".format(number), end="")
                printed += 1
                # Only separate by spaces if not at the last item
                if printed < len(sublist):
                    print(end=" ")
    print("")
