#!/usr/bin/python3

""" This is a module that is used to read content from a file specified as an argument filename"""
def read_file(filename=""):
    with open(filename , mode='r', encoding="utf-8") as myfile:
        """ The funtion open() is used to open the file in the read format and with the encoding of uft-8 """
        print(myfile.read(), end="")
    """ After the reading operation is done close the file"""    
    myfile.close()
