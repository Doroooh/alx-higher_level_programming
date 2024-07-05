#!/usr/bin/python3
"""
Script will take URL, send a request to the URL and display body of the response.

"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    addreqst = requests.get(url)

    if addreqst.status_code >= 400:
        print("Error code: {}".format(addreqst.status_code))
    else:
        print(addreqst.text)
