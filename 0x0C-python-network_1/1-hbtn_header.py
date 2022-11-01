#!/usr/bin/python3
"""
This module sends a request to a given
url and displays the X-Request-Id from the response's header
"""
from sys import argv
from urllib import request

if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        # print(response.read())
        print(response.info().get('X-Request-Id'))
