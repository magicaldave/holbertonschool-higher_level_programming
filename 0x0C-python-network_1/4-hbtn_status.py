#!/usr/bin/python3
"""
This module fetches an http site using requests
"""
from requests import get

if __name__ == '__main__':
    response = get('https://intranet.hbtn.io/status', timeout=10).text
    print(
        'Body response:',
        '- type: ' + str((type(response))),  # type of object from response
        '- content: ' + (response),  # raw content
        sep='\n\t')  # Adds newline and four spaces each time
