#!/usr/bin/python3
"""Script that takes a GitHub user name and password
and displays its id using GitHub api"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    user = 'https://api.github.com/user'
    author = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get(user, auth=author)
    print(req.json().get('id'))
