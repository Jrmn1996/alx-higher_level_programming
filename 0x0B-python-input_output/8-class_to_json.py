#!/usr/bin/python3
"""contains "class_to_json" func"""


def class_to_json(obj):
    """returns the dict description with simple data struct
    (list, dict, str, int and boolean)
    for JSON serialization of an onj"""
    return obj.__dict__
