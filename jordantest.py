#!/usr/bin/python3

# Jordan Hale Jan 2, 2019
# Script example for extracting metadata from dataverse based on Jess Whyte's
# function getID lists all returned objects under top dataverse_id
# then if 'type' == dataset, parses out dataset_id
# then runs function getMetadata which shows the dataset whose ID is passed
# output of getMetadata could be dumped in file for future work

import json
import requests

# --------------------------------------------------
# Update the 3 variables below to run this bash script 
# --------------------------------------------------
dataverse_server="demodv.scholarsportal.info" #demodv is the sandbox
# api_key="a5fdcbac-04d0-487b-8b55-79f2469cf211" #to get api key, create acct on dataverse, go to API Token, Create Token
dataverse_id="sp" #CHANGE for dataverse you want to work with

rows = 1000
start = 0
page = 1
condition = True
while (condition):
	dataverse_url = "https://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_id)
	returned_dataverses = requests.get(url = dataverse_url)
	metadata = json.loads(returned_dataverses.text)	
	print(metadata)
# 	for result in metadata['data']['items']:
# 		print(" - ", result['name'],"(" + result['type'] + ")," + result['identifier'])
# 		dataverse_ident = result['id'] # get ID for dataverses at root level
# 		dataverse_url = "http://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_ident)
# 		dataverse_info = requests.get(dataverse_url)
# 		dataverse_metadata = json.loads(dataverse_info.text)
# 		with open("dataverse_metadata.json", 'a') as outfile:
# 			json.dump(dataverse_metadata, outfile, sort_keys=True, indent=4)	
	 


# 
# 
# def main():
# 	# define source URL, just root dataverse contents
# 	urlData = "https://%s/api/dataverses/%s/contents" % (dataverse_server, dataverse_id)
# 	# open URL and read the data
# 	response = requests.get(url = urlData)
# 	if (response.status_code == 200):
# 		data = response.text
# 		printResults(data)
# 	else: 
# 		print("Received error, cannot parse results")
# 		print(response.status_code)
# 		
# main()
# 	
# 	