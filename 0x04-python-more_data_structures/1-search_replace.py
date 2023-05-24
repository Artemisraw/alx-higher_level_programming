#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    arr = search - 1
    for x in my_list:
        new_list.append(x)
    for x in new_list:
        if x is search:
            new_list[arr] = replace
        arr += 1
    return new_list
