#!/usr/bin/python3

""" Define class Square """


class Square:
    """Represents a square."""

    def __init__(self, size=0):

        """Initialize a new square.

        Args:
        size(int)
        """
        self.__size = size
        if type(size) != int:
            """ Checks if the type of size is int or not."""

            raise TypeError("size must be be an Integer")

        if size < 0:
            """ Check if the value of size is less than 0."""

            raise ValueError("size must be >= 0")
