#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(value) > 2 or len(value) < 2:
            raise TypeError("size must be an integer")


    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            
        print(("#" * self.__size + "\n")*self.__size)
