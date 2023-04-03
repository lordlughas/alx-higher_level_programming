#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ = "__main__":
    # create a varible for the argument
    url = sys.argv[1]

    # make the request
    r = requests.get(url)
    # display the information
    print(r.headers.get('X-Request-Id'))
