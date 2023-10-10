#!/usr/bin/python3
"""defines append_write func"""


def append_write(filename="", text=""):
    """appends filename with utf8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
