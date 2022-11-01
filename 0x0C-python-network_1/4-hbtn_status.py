#!/usr/bin/python3
"""
This module fetches an http site using requests
"""
import requests

if __name__ == '__main__':
    with requests.get('https://intranet.hbtn.io/status',
                      timeout=10) as response:
        response = response.content.decode('utf-8')
        print(
            'Body response:',
            '- type: ' + str((type(response))),  # type of object from response
            '- content: ' + (response),  # raw content
            sep='\n\t')  # Adds newline and four spaces each time
