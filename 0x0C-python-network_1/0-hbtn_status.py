#!/usr/bin/python3
"""This module fetches the status of an http site"""
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()
    print(
        'Body response:',
        '- type: ' + str(type(response)),  # type of object from response
        '- content: ' + str(response),  # raw content
        '- utf8 content: ' + response.decode('utf-8'),  # utf8 content
        sep='\n' + ' ' * 4)  # Adds newline and four spaces each time
