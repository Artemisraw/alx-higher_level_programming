#!/usr/bin/python3
"""This module holds a square class
    """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """new class inherits from rectangle
    Arguments:
        Rectangle {class} -- baseclass
    """

    def __init__(self, size):
        """size of new class square
        Arguments:
            size {[int]} -- size of the saquare
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of the square
        Returns:
            [int] -- the area of the square
        """
        return self.__size * self.__size
