#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = []

    for x in set_1:
        for i in set_2:
            if x is i:
                set_3.append(i)
    return set_3
