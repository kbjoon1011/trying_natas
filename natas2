#Import Library
import requests
import re

#Setting variables needed
username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
url = f'http://{username}.natas.labs.overthewire.org/files/users.txt'

#Connect to natas
session = requests.Session()
response = session.request('GET', url, auth=(username,password))

#Filtering to get a password
#result = response.text
result = re.findall('natas3:(.*)', response.text)[0]

print(result)
