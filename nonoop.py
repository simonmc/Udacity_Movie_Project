#used this to get the API request working before I did the Class Def
#This won't be in the finalised project 
import requests
import json

title = 'Star Wars: Episode IV - A New Hope'
OMDb_path = 'http://www.omdbapi.com/'
apikey = '73cd8d95'
payload = {'apikey': apikey,'t': title }
r = requests.get(OMDb_path, params = payload)
alldata = r.json()
