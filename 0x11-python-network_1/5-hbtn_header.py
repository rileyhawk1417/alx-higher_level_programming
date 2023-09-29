#!/usr/bin/python3
"""
Display X-Request-Id header from a given url
This time using requests
"""
import sys
import requests as req

if __name__ == "__main__":
    url = sys.argv[1]
    request = req.get(url)
    print(request.headers.get("X-Request-Id"))
