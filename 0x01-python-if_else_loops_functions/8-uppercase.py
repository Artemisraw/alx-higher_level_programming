#!/usr/bin/python3

def uppercase(str):
    result = ""
    for x in str:
        if ord(x) >= 97 and ord(x) < 123:
            result += chr(ord(x) - 32)
        else:
            result+=x
    print(result)