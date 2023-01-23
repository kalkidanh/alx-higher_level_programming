#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as n:
        sys.stderr.write("Exception: {}\n".format(n))
        return (False)
    else:
        return (True)
