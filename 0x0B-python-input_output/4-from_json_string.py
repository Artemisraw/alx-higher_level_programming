#!/usr/bin/python3
"""Module converts from json string to object"""
import json


def from_json_string(my_str):
    """funtion converts my_str to an object"""
    return json.loads(my_str)
