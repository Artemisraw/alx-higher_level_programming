#!/usr/bin/python3
"""Module that returns Json from string object"""

import json


def to_json_string(my_obj):
    """funtion that converts obj string to json"""
    return json.dumps(my_obj)
