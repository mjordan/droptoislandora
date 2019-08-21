#!/usr/bin/env python3

import os
import sys
import mimetypes
import requests

# Hard-coded (!) config variables. In a production tool, these would be stored/managed elsewhere.
host = "http://localhost:8000"
username = admin
password = islandora
media_use_tid = 16
content_type = islandora_object

# Absolute path to the file that was dropped on the shortcut.
filepath = sys.argv[1]

# Get some info about the file, so we can add it to the description field for demo purposes.




# Create the node.




# Add the media.
