#!/usr/bin/python3
"""Module that creates an object from Json file"""
import json


def load_from_json_file(filename):
    """funtion converts json from a file to an object"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        text = myFile.read()
        return json.loads(text)
