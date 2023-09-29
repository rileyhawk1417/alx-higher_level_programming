#!/usr/bin/python3
"""
Send a POST request to given URL then display response
in utf-8 encoding
"""
import sys
import urllib.parse as parser
import urllib.request as req

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    rawData = parser.urlencode(email).encode("ascii")
    request = req.Request(url, rawData)
    with req.urlopen(request) as res:
        print(res.read().decode("utf-8"))
