#!/usr/bin/python3
"""Script that sends a request to a URL and displays the body of the response."""

from sys import argv
import requests


if __name__ == '__main__':
    req = requests.get(argv[1])
    print('Error code: {}'.format(
        req.status_code)) if req.status_code >= 400 else print(req.text)
