#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Instantiating the class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Defining the getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """defing the getter size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Method that returns  the area of the square"""
        area = self.__size * self.__size

        return area

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            print(("#" * self.__size + "\n") * self.__size)
