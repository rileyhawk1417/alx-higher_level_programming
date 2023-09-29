#!/usr/bin/python3
"""
Send a POST request to given URL then display response
in utf-8 encoding
This time using requests
"""

import sys
import requests as req

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    request = req.post(url, data=email)
    print(request.text)
