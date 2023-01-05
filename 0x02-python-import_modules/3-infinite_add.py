#!/usr/bin/python3
""" prints the result of the addition of all arguments"""
if __name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
