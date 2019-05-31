import json
import requests

# Construct URL
dataverse_server = "demodv.scholarsportal.info"
api_key = "" # not required for demodv
dataverse_id = "sp" # change for dataverse you want to work with; for demodv, root = "sp" 

# Generate list of dataverse IDs
def get_request():
	iterate_url = "http://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_id)
	contents_read = requests.get(url = iterate_url)
	contents_store = json.loads(contents_read.text)
	with open('full_contents.json', 'w') as outfile:
		json.dump(contents_store, outfile, sort_keys=True, indent=4) # Generate full contents list for top level
	for each in contents_store['data']:
		while each['type'] == "dataverse": # For the sub-dataverses
			if each['type'] == "dataset":
				dataset_id = each['id']
				get_metadata(dataset_id)
				
# Get dataverse json metadata for each dataset
def get_metadata(dataset_id):
	dataset_url = "http://%s/api/datasets/%s?key=%s" % (dataverse_server, dataset_id, api_key)
	contents_read = requests.get(dataset_url)
	dataset_store = json.loads(contents_read.text)
	print(dataset_store)
	with open('dataset_contents.json', 'w') as outfile:
		json.dump(dataset_store, outfile, sort_keys=True, indent=4)

# # Export other metadata formats
# def export_metadata(dataset_id, export_format):
# 	export_format = ["ddi", "oai_ddi", "dcterms", "oai_dc", "schema.org"]
# 	persistentId = 

get_request()
		
