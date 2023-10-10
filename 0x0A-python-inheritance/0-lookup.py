#!/usr/bin/python3
"""module for lookup func"""


def lookup(obj):
    """looks up object attributes and methods
    args:
    the object to list
    return:
    list object
    """
    return dir(obj)
