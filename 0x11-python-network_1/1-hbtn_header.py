#!/usr/bin/python3
"""Script that takes in a URL as arg, sends a request to the URL and
returns the value of the X-Request-Id variable of the header"""
from sys import argv
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen(argv[1]) as request:
        print(request.headers.get('X-Request-Id'))
