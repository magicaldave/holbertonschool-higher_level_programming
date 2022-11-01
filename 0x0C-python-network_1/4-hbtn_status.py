#!/usr/bin/python3
"""This module fetches the status of an http site"""
import requests

with requests.get('https://intranet.hbtn.io/status', timeout=10) as response:
    print(
        'Body response:',
        '- type: {}'.format(type(
            response.content.decode('utf-8'))),  # type of object from response
        '- content: {}'.format(
            response.content.decode('utf-8')),  # raw content
        sep='\n\t')  # Adds newline and four spaces each time
