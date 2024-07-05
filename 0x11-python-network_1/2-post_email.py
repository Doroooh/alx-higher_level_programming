#!/usr/bin/python3
"""Sending the POST request to a URL with a email.
displaying the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    dataval = urllib.parse.urlencode(val).encode("ascii")

    addreqst = urllib.request.Request(url, dataval)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
