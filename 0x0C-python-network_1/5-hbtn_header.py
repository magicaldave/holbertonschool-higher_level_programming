#!/usr/bin/python3
"""
This module sends a request to a given
url and displays the X-Request-Id from the response's header
"""
from sys import argv
from requests import get

if __name__ == '__main__':
    response = get(argv[1], timeout=10)
    print(response.headers.get('X-Request-Id'))
