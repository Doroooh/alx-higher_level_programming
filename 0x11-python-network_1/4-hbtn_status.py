#!/usr/bin/python3

"""
the script to get https://alx-intranet.hbtn.io/status with
the request, printing response to stdout
"""

from requests import get


def get_alx_intranet(url='https://alx-intranet.hbtn.io/status'):
"""
Sending  GET request to  url, printing the response
"""
    resrq = get(url)
    print("Body response:")
    print("\t- type: {}".format(str(resrq).__class__))
    print("\t- content: {}".format(resrq.text))

if __name__ == "__main__":
    get_alx_intranet()
