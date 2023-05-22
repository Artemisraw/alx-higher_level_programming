#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list ==  None:
        return
    else:
        x = len(my_list)
        while x >= 1:
            x = x - 1
            print("{:d}".format(my_list[x]))
