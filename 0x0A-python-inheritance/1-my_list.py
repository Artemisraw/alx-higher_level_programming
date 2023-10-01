#!/usr/bin/python3
"""Module that holds MyList class to sort a list
    """


class MyList(list):
    """ class that inherits from list
    Arguments:
        list {[list]} -- Parent class
    """

    def print_sorted(self):
        """Prints a new list sorted based on the object intanced
        """
        print(sorted(self))
