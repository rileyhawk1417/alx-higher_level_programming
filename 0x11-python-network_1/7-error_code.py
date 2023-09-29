#!/usr/bin/python3
"""
Send request to url then print body response
In this case print an error
Also use Requests & flag if the error is less than 400
"""
import sys
import requests as req


if __name__ == "__main__":
    url = sys.argv[1]
    request = req.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
