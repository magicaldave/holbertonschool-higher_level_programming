#!/usr/bin/python3
"""
This module sends a request to a given
url and displays the X-Request-Id from the response's header
"""
from sys import argv
from urllib import request

with request.urlopen(argv[1]) as response:
    print(response.info()['X-Request-Id'])
