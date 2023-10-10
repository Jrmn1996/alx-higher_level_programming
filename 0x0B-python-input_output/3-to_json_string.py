#!/usr/bin/python3
"""defines to_json_string func"""


import json


def to_json_string(my_obj):
    """returns json representaion of an obj"""
    return json.dumps(my_obj)
