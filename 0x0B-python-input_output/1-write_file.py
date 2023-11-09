#!/usr/bin/python3
""" This is a module that is used for writing a file. """


def write_file(filename="", text=""):
    """Funtion that writes the text in the specified file"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        print(myfile.write(text))
