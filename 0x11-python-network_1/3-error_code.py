#!/usr/bin/python3
"""Script that takes a URL sends a request and displays the body
of the response"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urlopen(Request(argv[1])) as request:
            print(request.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
