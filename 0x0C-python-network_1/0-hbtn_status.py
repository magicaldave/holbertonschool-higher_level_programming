#!/usr/bin/python3
"""This module fetches the status of an http site"""
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()
    print(
        'Body response:',
        '- type: {}'.format(type(response)),  # type of object from response
        '- content: {}'.format(response),  # raw content
        '- utf8 content: {}'.format(response.decode('utf8')),  # utf8 content
        sep='\n\t')  # Adds newline and four spaces each time
