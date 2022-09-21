#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 123:
            x = ord(ch) - 32
            y = chr(x)
            new_str += y
        else:
            new_str += ch
    print("{}".format(new_str))
