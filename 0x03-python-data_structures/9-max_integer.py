#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    sorted_list = my_list.copy()
    sorted_list.sort()
    return sorted_list[-1]
