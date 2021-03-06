#!/usr/bin/python3

# Jess Whyte Jun 15, 2018
# Script example for extracting metadata from dataverse
# function getID lists all returned objects under top dataverse_id
# then if 'type' == dataset, parses out dataset_id
# then runs function getMetadata which shows the dataset whose ID is passed
# output of getMetadata could be dumped in file for future work

import json
import requests # may need to install 'requests', e.g. pip install requests
import socket

# --------------------------------------------------
# Update the 3 variables below to run this bash script 
# --------------------------------------------------
dataverse_server="demodv.scholarsportal.info" #demodv is the sandbox
api_key="a5fdcbac-04d0-487b-8b55-79f2469cf211" #to get api key, create acct on dataverse, go to API Token, Create Token
dataverse_id="root" #CHANGE for dataverse you want to work with


def getID():
	print ("running getstuff...") #print for test
	URL = "http://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_id) # List all objects under dataverse_id
	response = requests.get(url = URL)
	stuff = json.loads(response.text)
	for result in stuff['data']: #for any returned results
		while ((result['type'])=="dataverse"):
			if (result['type'])=="dataset":
				dataset_id = (result['id']) #dataset_id = 'id' key
				getMetadata(dataset_id) #run getMetadata and pass dataset_id
#			else:
#				pass

			


## function for retrieving metadata based on dataset_id
def getMetadata(dataset_id):
	URL = "http://%s/api/dataverses/%s?key=%s" % (dataverse_server, dataset_id, api_key)
	response = requests.get(url = URL)
	data = json.loads(response.text)
	print(data) # print json response to screen, can direct to file
	with open('datazzz.json', 'a') as outfile:
                json.dump(data, outfile, sort_keys=True, indent=4)  
        

### script below

getID()
