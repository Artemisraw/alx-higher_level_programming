#!/usr/bin/python3
""" This is a module that is used to read content from a file specified as an argument filename."""


def read_file(filename=""):
    """ Funtion that uses the filename as an argument when reading from a file"""
    with open(filename , mode='r', encoding="utf-8") as myfile:
        print(myfile.read(), end="")
    """ After the reading operation is done close the file"""    
    myfile.close()
