#!/usr/bin/python3
"""This module holds a class Rectangle
    """
base_geo = __import__("7-base_geometry").BaseGeometry


class Rectangle(base_geo):
    """class rectangle that inherits from BaseGeometry
    Arguments:
        base_geo {[class]} -- Baseclass
    """

    def __init__(self, width, height):
        """Constructor or initializer
        Arguments:
            width {[int]} -- width of the rectangle
            height {[int]} -- height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of the rectangle
        Returns:
            [int] -- the area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """printable string
        Returns:
            [str] -- rectangle representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
