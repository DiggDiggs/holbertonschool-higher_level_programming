#!/usr/bin/python3
"""0-add_integer.py and test/0-add_integer.txt"""


def add_integer(a, b=98):
    """Add integer"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)


"""this is where the a, b are"""
return a + b
