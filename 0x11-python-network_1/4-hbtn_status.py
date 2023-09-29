#!/usr/bin/python3
"""
Fetch the status from URL https://alx-intranet.hbtn.io/status
"""
import requests as req

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = req.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
