#!/usr/bin/env bash
# Get content length using curl then print it
# Not sure on how to use grep on this
curl -sI "$1" | awk '/Content-Length/{print $2}'
