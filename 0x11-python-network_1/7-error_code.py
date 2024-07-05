#!/usr/bin/python3
"""Sending the request to an URL then  displaying the response body.

Usage: ./7-error_code.py <URL>
this is for handling the HTTP errors.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    a = requests.get(url)
    if a.status_code >= 400:
        print("Error code.{} format(a.status_code))
    else:
        print(a.text)
