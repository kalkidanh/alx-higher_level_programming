#!/usr/bin/python3
"""Script that takes a URL and email address, sends a POST request to the
URL with email as a parameter and displays the body of the response."""

from sys import argv
import requests


if __name__ == '__main__':
    email = {'email': argv[2]}
    req = requests.post(argv[1], data=email)
    print(req.text)
