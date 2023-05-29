#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        result = []
        for i in range(x):
            if i != x:
                result.append(i)
            print("{:d}".format(result[i]), end="")
    except TypeError:
        print("Error: Invalid value")
    return result
