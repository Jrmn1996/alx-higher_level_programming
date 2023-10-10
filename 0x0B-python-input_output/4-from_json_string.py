#!/usr/bin/python3
"""defines from_json_string func"""


import json


def from_json_string(my_str):
    """return json string"""
    return json.loads(my_str)
