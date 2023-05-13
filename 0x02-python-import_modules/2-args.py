#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    size = len(args)

    if size == 1:
        print("{} arguments".format(size - 1))
    if size > 1:
        print("{} arguments".format(size - 1))
        for i in range(1, size):
            print("{}: {}".format(i, args[i]))
