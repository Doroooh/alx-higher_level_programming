#!/usr/bin/python3
"""
Displaying the X-Request-Id header variable of the request to the given URL.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    addreqst = requests.get(url)
    print(addreqst.headers.get("X-Request-Id"))
