#!/usr/bin/env bash
# Display all the HTTP methods in the URL
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{print $2}'
