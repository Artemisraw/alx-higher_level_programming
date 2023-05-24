#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    arr = search - 1
    for x in my_list:
        new_list.append(x)
    count = 0
    for x in new_list:
        if x is search:
            new_list[count] = replace
        count += 1
    return new_list
