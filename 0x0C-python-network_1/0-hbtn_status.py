#!/usr/bin/python3
"""This module fetches the status of an http site"""
from urllib import request

if __name__ == '__main__':
    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf-8')))
        # Adds newline and four spaces each time
