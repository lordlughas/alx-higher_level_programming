#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys


if __name__ = "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = requeset.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = request.read()
        print(body.decode('utf-8'))
