#!/usr/bin/python3
"""Module that saves Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Funtion that save the object to a file"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        teststr = json.dumps(my_obj)
        myfile.write(teststr)
