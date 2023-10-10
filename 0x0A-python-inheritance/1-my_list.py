#!/usr/bin/python3
"""module for Mylist class"""


class MyList(list):
    """custom Mylist class"""
    def print_sorted(self):
        """method for printing sorted list"""
        print(sorted(self))
