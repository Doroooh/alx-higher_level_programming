#!/usr/bin/python3
"""
This script will take the URL, sending the request to URL, and displaying
values of X-request-Id variable in the response header.
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    addreqst = Request(url)

    with urlopen(addreqst) as response:
        print(dict(response.headers).get("X-Request-Id"))
