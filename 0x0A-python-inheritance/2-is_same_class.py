#!/usr/bin/python3
"""Module with function to check if an
    objects is exacly from a specific class
    """


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    Arguments:
        obj {[object]} -- object to check
        a_class {[class]} -- specific class
    Returns:
        [bool] -- True or false if is the same class
    """
    return type(obj) == a_class
