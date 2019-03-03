#Import Library
import requests
import re

#Setting variables needed
username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'
url = f'http://{username}.natas.labs.overthewire.org/'

#Connect to natas
session = requests.Session()
response = session.request('GET', url, auth=(username,password))

#Filtering to get a password
result = re.findall('<!--The password for natas[0-9?] is (.*) -->', response.text)[0]

print(result)
