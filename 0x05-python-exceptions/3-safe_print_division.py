#!/usr/bin/python3

def safe_print_division(a, b):
    result = None

    try:
        if a < 0 or b < 0:
            raise ZeroDivisionError
        result = a / b
        return result
    except ZeroDivisionError:
        return result

    finally:
        print("Incide result: {}".format(result))
