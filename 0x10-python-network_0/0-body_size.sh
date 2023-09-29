#!/bin/bash
# Get content length using curl then print it, unsure on how to use grep
curl -sI "$1" | awk '/Content-Length/{print $2}'
