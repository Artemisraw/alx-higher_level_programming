#!/usr/bin/python3
"""Module that appends text to the file"""


def append_write(filename="", text=""):
    """funtion that appends text to a file"""
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
