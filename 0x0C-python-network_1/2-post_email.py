#!/usr/bin/python3
"""
This module sends a request to a url and gets a user email
"""
from sys import argv
from urllib import request, parse

if __name__ == '__main__':
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read())
