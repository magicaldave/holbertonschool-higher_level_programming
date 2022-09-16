#!/usr/bin/python3
"""
BaseGeometry initial module
"""


class BaseGeometry():
    """Nobody expects the Spanish Inquisition!"""

    def area(self):
        """Well, it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validated input to the class"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
