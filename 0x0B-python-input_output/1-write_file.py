#!/usr/bin/python3
"""defines write_file with 2 args"""


def write_file(filename="", text=""):
    """reads filename with utf8"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
