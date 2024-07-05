#!/usr/bin/python3
"""Sending the request to a url then  printing responses"""

from requests import get
from sys import argv


def request_header_property(url: str) -> str:
"""sending the requests to URL, and getting responses
   , also handles exceptions  Args
   url (str) is the URL to query
"""
    response = get(url)
    if int(response.status_code) >= 400:
        return ("Error code: {}".format(response.status_code))
    return response.text
if __name__ == "__main__":
    print(request_header_property(argv[1]))
