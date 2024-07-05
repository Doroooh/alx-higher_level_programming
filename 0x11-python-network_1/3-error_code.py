#!/usr/bin/python3
"""
Script to take in a URL, sending thea request to URL and displaying
body of the response (decoded in utf-8).
 Handleing HTTP errors.
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    addreqst = Request(url)

    try:
        with urlopen(addreqst) as response:
            print(response.read().decode("ascii"))
    except HTTPError as s:
        print("Error code: {}".format(s.code))
