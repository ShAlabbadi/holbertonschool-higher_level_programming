#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list, and then save them to a file"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_check = len(sys.argv)

try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

for x in range(1, arg_check):
    my_list.append(sys.argv[x])

save_to_json_file(my_list, 'add_item.json')
