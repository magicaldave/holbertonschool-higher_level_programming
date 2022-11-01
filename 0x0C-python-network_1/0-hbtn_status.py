#!/usr/bin/python3
"""This module fetches the status of an http site"""
from urllib import request

if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
        print(
            'Body response:',
            '- type: ' + str(type(response)),  # type of object from response
            '- content: ' + str(response),  # raw content
            '- utf8 content: ' + response.decode('utf-8'),  # utf8 content
            sep='\n\t')  # Adds newline and four spaces each time
