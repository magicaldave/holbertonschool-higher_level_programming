#!/usr/bin/python3
"""
Writes a list in JSON format to a text file
"""

# Standard Modules
import sys
# My Modules
load_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file
l_file = "add_item.json"

# Load it, or empty list if not
try:
    ArgStack = load_json(l_file)
except (FileNotFoundError, TypeError):
    ArgStack = []

# Append individually to prevent nested lists
for arg in sys.argv[1:]:
    ArgStack.append(arg)

save_json(ArgStack, l_file)
