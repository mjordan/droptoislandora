#!/usr/bin/env python3

import os
import sys
import mimetypes
import requests
import subprocess

# Hard-coded (!) config variables. In a production tool, these would be stored/managed elsewhere.
host = "http://localhost:8000"
username = "admin"
password = "islandora"
media_use_tid = "16"
content_type = "islandora_object"

# Absolute path to the file that was dropped on the shortcut.
filepath = sys.argv[1]

# TIFFs and JP2s are 'file', as is everything else not in these lists.
image_mimetypes = ['image/jpeg', 'image/png', 'image/gif']
audio_mimetypes = ['audio/mpeg3', 'audio/wav', 'audio/aac']
video_mimetypes = ['video/mp4']
mimetypes.init()

# Note: Taxonomy IDs for "Islandora Models" are hard coded here.
# Also, TIFFs and JP2s will be assigned a "Binary" model.
mimetype = mimetypes.guess_type(filepath)
media_type = 'file'
node_model_tid = '22'
if mimetype[0] in image_mimetypes:
    media_type = 'image'
    node_model_tid = '24'
if mimetype[0] in audio_mimetypes:
    media_type = 'audio'
    node_model_tid = '21'
if mimetype[0] in video_mimetypes:
    media_type = 'video'
    node_model_tid = '25'

# Get some info about the file, so we can add it to the description field for demo purposes.




# Create the node.
node_headers = {
    'Content-Type': 'application/json'
}
url = host + '/node?_format=json'
filename = os.path.basename(filepath)
node_json = {
    'type': [
        {'target_id': content_type,
         'target_type': 'node_type'}
    ],
    'title': [
        {'value': filename}
    ],
    'field_model': [
        {'target_id': node_model_tid,
         'target_type': 'taxonomy_term'}
    ],
    'field_description': [
        {'value': "Ingested using the 'Drop to Islandora' prototype tool."}
    ],    
}

node_response = requests.post(
    url,
    auth=(username, password),
    headers=node_headers,
    json=node_json
)
if node_response.status_code == 201:
    node_uri = node_response.headers['location']
else:
	subprocess.call(['notify-send', 'Error!', 'Islandora object not created'])
	sys.exit

# If there is a media file, add it.
if node_response.status_code == 201:
	media_endpoint_path = ('/media/' +
	                       media_type +
	                       '/' + media_use_tid)
	media_endpoint = node_uri + media_endpoint_path
	file_destination = 'fedora://' + os.path.basename(filepath)
	media_headers = {
	    'Content-Type': mimetype[0],
	    'Content-Location': file_destination
	}
	binary_data = open(filepath, 'rb')
	media_response = requests.put(
            media_endpoint,
            auth=(username, password),
            headers=media_headers,
            json='',
            data=binary_data
            )

	allowed_media_response_codes = [201, 204]
	if media_response.status_code in allowed_media_response_codes:
	    subprocess.call(['notify-send','Islandora object created', node_uri])
