#!/usr/bin/python3
"""Module that holds a funtion that adds a
    new attribute to an object if it’s possible
    """


def add_attribute(add_obj, name, value):
    """Add a new attribute to an object if it is possible
    Arguments:
        add_obj {[obj]} -- Object whose attribute has to be set
        name {[str]} -- Attribute name
        value {[]} -- Value given to the attribute
    Raises:
        TypeError: can't add new attribute
    """
    if hasattr(add_obj, "__dict__"):
        setattr(add_obj, name, value)
    else:
        raise TypeError("can't add new attribute")
