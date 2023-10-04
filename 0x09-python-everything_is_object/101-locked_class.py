#!/usr/bin/python3
"""defines a lockedclass"""
class LockedClass:
    """
    prevents user from instantiating new lockedclass attr
    for anything but the attr called "first name"
    """
    __slots__ = ["first name"]
