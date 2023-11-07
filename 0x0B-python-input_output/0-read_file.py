#!/usr/bin/python3

def read_file(filename=""):
    f = open(filename, 'r', encoding="UTF8")
    print(f.read())
    f.close()
