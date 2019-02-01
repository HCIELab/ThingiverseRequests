#####################################################################
# Sample code for downloading "thing" IDs based on search keyword
# For more search options, visit https://www.thingiverse.com/developers/rest-api-reference
#####################################################################

import requests, json, csv

# HEADERS
# put authorization code here  - change only the "Authorization" field
headers = {
	"Authorization": "Bearer 10ff57f6e7580997cace5d8476b2679f",
	"Host": "api.thingiverse.com",
	"Content-Type": "application/json; charset=utf-8"
}

#################################
##### INITIALIZE VARIABLES ######

# Initialize page range to search within
page_num=10

# Global Variables
stuff=[]
all_objects = []

ids = []
versioned = []
dicts = []

# put search keywords here
keywords = ["case", "holder"]


###########################
##### HELP FUNCTIONS ######

def make_page_lists(kword):
	global stuff

# method that does a GET request, receives JSON data, turns them into dictionaries, and stores them in an array
	for i in range(1,page_num +1):  
		for z in range(len(keywords)):
			global stuff
			try:
				r= requests.get(url ='https://api.thingiverse.com/search/'+ str(keywords[z])+ '?page=' + str(i) + '&per_page=5', headers=headers).json()
				# prevent JSON decoding errors
				print (type(r[0]))
			except ValueError:
				print ('Decoding JSON has failed')

		# append response items into an array
		stuff.append(r)

# Previous method creates arrays -- the following method concatenates them
def merge_page_lists():
	global all_objects
	for i in range(0,len(stuff)):
		if (type(stuff[i])) == list:
			all_objects = all_objects + stuff[i]


##########################
##### MAIN FUNCTION ######

for i in range(0, len(keywords)):
	make_page_lists(i)
	merge_page_lists()
	print(all_objects)



