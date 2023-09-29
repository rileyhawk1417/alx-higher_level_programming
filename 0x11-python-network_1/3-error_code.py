#!/usr/bin/python3
"""
Send request to url then print body response
In this case print an error
"""
import sys
import urllib.error as urlError
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]
    request = req.Request(url)
    try:
        with req.urlopen(request) as res:
            print(res.read().decode("ascii"))
    except urlError.HTTPError as err:
        print("Error code: {}".format(err.code))
