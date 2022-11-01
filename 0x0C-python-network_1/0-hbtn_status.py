#!/usr/bin/python3
"""This module fetches the status of an http site"""
from urllib import request

req = request.Request('https://intranet.hbtn.io/status')
with request.urlopen(req) as response:
    response = response.read()
    print('Body response:')
    print('\t- type: {}'.format(
        type(response)))  # type of object from response
    print('\t- content: {}'.format(response))  # raw content
    print('\t- utf8 content: {}'.format(
        response.decode('utf8')))  # Adds newline and four spaces each time
