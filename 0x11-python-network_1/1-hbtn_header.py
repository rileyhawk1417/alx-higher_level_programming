#!/usr/bin/python3
"""Display X-Request-Id header from a given url"""
import sys
import urllib.request as req

if __name__ == "__main__":
    url = sys.argv[1]
    request = req.Request(url)
    with req.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
