#!/usr/bin/python3
"""This script will fetch https://intranet.hbtn.io/status"""

import urllib.request

def fetch_status(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

if __name__ == "__main__":
    fetch_status("https://intranet.hbtn.io/status")
