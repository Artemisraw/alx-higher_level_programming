#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    set_3 = a_dictionary.copy()

    for x in set_3:
        set_3[x] = set_3[x] * 2
    return set_3
