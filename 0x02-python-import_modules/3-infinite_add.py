#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    result = 0
    for arg in args:
        x = int(arg)
        result = result + x
    print(result)
