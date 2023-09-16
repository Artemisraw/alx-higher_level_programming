#!/usr/bin/python3

""" Defining A class Square. """


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Instantiation of the Class Square"""

        self.__size = size

        if type(size) is not int:
            """Checks if size is an integer"""

            raise TypeError("size must be an integer")

        if size < 0:
            """checks if size is less than 0"""

            raise ValueError("size must be >= 0")

    def area(self):
        """funtion that returns the area of the square

        Args:
            area(int) shows the size of the square
        """
        area = self.__size * self.__size

        return area
