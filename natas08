#Import Library
import requests
import re
import base64
import binascii

#Setting variables needed
username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = f'http://{username}.natas.labs.overthewire.org/'

#Translating the secret value
key = base64.b64decode(binascii.a2b_hex('3d3d516343746d4d6d6c315669563362')[::-1])

payloads = {'secret': key ,'submit':'submit'}

#Connect to natas
session = requests.Session()
response = session.request('POST', url, auth=(username,password), data=payloads)

#Filtering to get a password
result = response.text
result = re.findall('Access granted. The password for natas9 is (.*)', response.text)[0]

print(result)
