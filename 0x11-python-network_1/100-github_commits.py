#!/usr/bin/python3
"""Script that returns the last 10 commits using GitHub API"""

from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    request = requests.get(url)
    res = request.json()
    for line in res[:10]:
        print('{}: {}'.format(line.get('sha'),
                              line.get('commit').get('author').get('name')))i
