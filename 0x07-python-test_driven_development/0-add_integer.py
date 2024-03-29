#!/usr/bin/python3
"""
This is the "0-add_integer" module,

the 0-add_integer module supplies one funtion, add_integer(a,b=98).
"""
def add_integer(a,b=98):
    """result is the addition of a and b."""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an intenger')
    if type(b) is not int and type(b) is not float:
        raise TypeError ('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
