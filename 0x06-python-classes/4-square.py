#!/usr/bin/python3

"""Defining a class Square"""


class Square:
    def __init__(self, size=0):
        """Initializing the clsaa

        Args:
        size(int) size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the method size """

        if type(value) != int:
            """ Checks if the size is an integer"""
            raise TypeError("size must be an integer")

        if value < 0:
            """Checks if size is less than 0"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the are of the Square"""
        area = self.__size * self.__size

        return area
