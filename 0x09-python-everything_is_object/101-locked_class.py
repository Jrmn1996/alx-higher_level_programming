#!/usr/bin/python3
"""defines a locked class"""
class LockedClass:
    """
    prevents user from instantiating new lockedclass attr
    for anything but attr called 'first name'
    """
    __slots__ = ["first name"]
