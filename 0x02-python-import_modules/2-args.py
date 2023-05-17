vi #!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argCount = len(argv)
    if argCount == 1:
        print(f"0 arguments.")
    if argCount > 1:
        if argCount == 2:
            print(f"1 argument:")
        else:
            print(f"{argCount - 1} arguments:")
    for i in range(1, argCount):
        print(f"{i}: {argv[i]}")
