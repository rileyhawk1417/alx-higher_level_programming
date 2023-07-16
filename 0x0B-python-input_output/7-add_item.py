#!/usr/bin/python3

"""
Python script that appends items to a file if exists.
If it doesn't exist then it will create the file
"""

import os.path
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

fileName = "add_item.json"
input_list = []

if os.path.exists(fileName):
    input_list = load_from_json_file(fileName)
    input_list.append("clicky")
    print(input_list)

for idx in range(1, len(sys.argv)):
    input_list.append(sys.argv[idx])

save_to_json_file(input_list, fileName)
