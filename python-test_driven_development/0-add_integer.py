#!/usr/bin/python3
"""0-add_integer.py and test/0-add_integer.txt"""


def add_integer(a, b=98):
    """
    adds an interger 
    to test/0-add_integer.txt
    check that error type
    """
    if not isinstance(b, int):
        if not isinstance(b, float):
            b= int(b)
        else:
            raise typeError("b must be an integer")
    return a + b
