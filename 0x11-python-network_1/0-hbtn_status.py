#!/usr/bin/python3
"""Script that fetches the webpage using urllib module"""
from urllib import request

if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf8')))
