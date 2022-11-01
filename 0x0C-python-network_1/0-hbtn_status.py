#!/usr/bin/env python3
"""This module fetches the status of an http site"""
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    response = response.read()
    print(
        'Body response:',
        f'- type: {type(response)}',  # type of object from response
        f'- content: {response}',  # raw content
        f'- utf8 content: {response.decode("utf-8")}',  # utf8 content
        sep=f'\n{chr(32) * 4}')  # Adds newline and four spaces each time
