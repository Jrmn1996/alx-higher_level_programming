#!/usr/bin/python3
"""contains class student"""


class Student:
    """rep of a student"""
    def __init__(self, first_name, last_name, age):
        """initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dict rep of a student instance
        if attrs is a list of strs, only attr names contained in this
        list must be retrieved
        otherwise all attr must be retrieved
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, calue in self.__dict__.itrms():
            if key in attrs:
                my_dict[key] = value
        return my_dict
