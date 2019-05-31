#!/usr/bin/python3

import json
import requests
import xml.etree.ElementTree as ET
from os import path

# Construct URL
dataverse_server = "demodv.scholarsportal.info"
api_key = "" # not required for demodv
dataverse_id = "sp" # change for dataverse you want to work with; for demodv, root = "sp" 
# it should be the highest level dv you're interested in

# Generate list of datasets
def get_request(dataverse_server, dataverse_id):
	iterate_url = "http://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_id)
	contents_read = requests.get(url = iterate_url)
	contents_store = json.loads(contents_read.text)
	with open('contents.json', 'a') as outfile:
		json.dump(contents_store, outfile, sort_keys=True, indent=4) # Generate full contents list for top level
	for each in contents_store:
		get_datasets(contents_store)

def get_datasets(contents_store):
	for each in contents_store['data']:
		if each['type'] == "dataset":
			http_id = each['persistentUrl']
			protocol = each['protocol']
			if protocol == "doi":
				persistentId = http_id.split("doi.org/",1)[1]
			elif protocol == "hdl":
				persistentId = http_id.split("handle.net/",1)[1]
				print(persistentId)
			get_metadata(persistentId, protocol)
		elif each['type'] == "dataverse":
			dataverse_id = each['id']
			get_request(dataverse_server, dataverse_id)


def get_metadata(persistentId, protocol):
	metadata_format = "dcterms" # change for different metadata formats
	dataset_url = "http://%s/api/datasets/export?exporter=%s&persistentId=%s:%s" % (dataverse_server, metadata_format, protocol, persistentId)
	print(dataset_url)
	r = requests.get(dataset_url)
	dataset_contents = r.text
	filename = persistentId.replace("/","_") + ".xml"
	outputpath = path.join(path.dirname(__file__), filename)
	with open(outputpath, 'w+') as f:
		f.write(dataset_contents)


get_request(dataverse_server, dataverse_id)
