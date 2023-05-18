#!/usr/bin/python3
"""This Module creates,Square that defines a square"""


class Square:
    """
    A class that represents a square.
    Attribuyes:
        --size (int): THE size of the square.
    """
    def __init__(self, size):
        """
        Initialize a new instance of the square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
