#Import Library
import requests
import re

#Setting variables needed
username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
#url = f'http://{username}.natas.labs.overthewire.org/robots.txt'
#url = f'http://{username}.natas.labs.overthewire.org//s3cr3t'
url = f'http://{username}.natas.labs.overthewire.org//s3cr3t/users.txt'

#Connect to natas
session = requests.Session()
response = session.request('GET', url, auth=(username,password))

#Filtering to get a password
#result = response.text
result = re.findall('natas4:(.*)', response.text)[0]

print(result)
