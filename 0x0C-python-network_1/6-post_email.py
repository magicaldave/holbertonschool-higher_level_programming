#!/usr/bin/python3
"""
This module takes a url and email, sends a POST request to that URL,
and displays the body of the response.
"""
from sys import argv
from requests import post

if __name__ == '__main__':
    response = post(argv[1], data={'email': argv[2]}, timeout=10).text
    print(response)
