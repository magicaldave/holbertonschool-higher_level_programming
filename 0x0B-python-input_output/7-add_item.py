#!/usr/bin/python3
"""
3-to_json_string module
"""

# Standard Modules
import sys
# My Modules
load_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file
l_file = "add_item.json"

try:
    ArgStack = load_json(l_file)
except:
    ArgStack = []
for arg in sys.argv[1:]:
    ArgStack.append(arg)
save_json(ArgStack, l_file)
