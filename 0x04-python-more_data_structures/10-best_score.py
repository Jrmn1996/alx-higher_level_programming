#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxkey = None
    maxval = 0
    for k, v in a_dictionary.items():
        if v > maxval:
            maxval = v
            maxkey = k
    return maxkey
