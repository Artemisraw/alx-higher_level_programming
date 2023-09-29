#!/usr/bin/python3
""" Base """
class Base:

    __nb_objects = 0

    def __init__(self, id=None):

        self.id = id

        if id is not None:
            id = self.id
        
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
