
#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for item in range(0, x):
            print("{}".format(my_list[item]),end="")
            n += 1
    except IndexError:
        pass
    print()
    return n
