#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    arr = search - 1
    for x in my_list:
        new_list.append(x)
    for x in new_list:
        if x is search:
            arr = x - 1
            new_list[arr] = replace
    return new_list
