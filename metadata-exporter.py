#!/usr/bin/python3

import json
import requests
import xml.etree.ElementTree as ET

# Construct URL
dataverse_server = "demodv.scholarsportal.info"
api_key = "" # not required for demodv
dataverse_id = "sp" # change for dataverse you want to work with; for demodv, root = "sp" 
# it should be the highest level dv you're interested in

# Generate list of datasets
def get_request():
	iterate_url = "http://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_id)
	contents_read = requests.get(url = iterate_url)
	contents_store = json.loads(contents_read.text)
	with open('contents.json', 'w') as outfile:
		json.dump(contents_store, outfile, sort_keys=True, indent=4) # Generate full contents list for top level
	for each in contents_store['data']:
		if each['type'] == "dataset":
			http_id = each['persistentUrl']
			persistentId = http_id[-18:]
			print(persistentId)
			protocol = each['protocol']
			get_metadata(persistentId, protocol)


def get_metadata(persistentId, protocol):
	metadata_format = "ddi" # change for different metadata formats
	dataset_url = "http://%s/api/datasets/export?exporter=%s&persistentId=%s:%s" % (dataverse_server, metadata_format, protocol, persistentId)
	print(dataset_url)
	dataset_contents = requests.get(dataset_url)
	pid = str(persistentId)
	f = open(pid + ".xml", "wb")
	f.write(dataset_contents.text)

	# root = ET.fromstring(dataset_contents.text)
	# print(root)
	
	

get_request()
