#!/usr/bin/python3
"""Script that takes a URL and email, sends a POST request to the URL with
the email as a parameter and displays the body of the response"""

from sys import argv
from urllib.parse import urlencode
from urllib.request import urlopen, Request

if __name__ == '__main__':
    email = {'email': argv[2]}
    data = urlencode(email).encode('utf-8')
    with urlopen(Request(argv[1], data)) as request:
        print(request.read().decode('utf-8'))
