#!/usr/bin/python3
"""
This module sends a request to a url and gets a user email
"""
from sys import argv
from urllib import request, error

if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as htmlfail:
        print("Error code: " + str(htmlfail.code))
