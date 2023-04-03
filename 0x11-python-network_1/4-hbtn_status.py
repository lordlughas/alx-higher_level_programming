#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using request package
"""
import requests


if __name__ = "__main__":
    # making the GET request to the url
    r = requests.get('https://alx-intranet.hbtn.io/status')

    # printing information about the response
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
