#Import Library
import requests
import re
import base64

#This method is to find a key
def findingKey():
    result = ''
    data = '{"showpassword":"no","bgcolor":"#ffffff"}'
    cookies = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='
    for c1, c2 in zip(data, base64.b64decode(cookies)):
        result = result + chr(ord(c1) ^ c2)
    return result

#This method is to find a correct cookie
def xorEnc():
    result=''
    key = 'qw8J'
    data = '{"showpassword":"yes","bgcolor":"#ffffff"}'
    for i in range(len(data)):
        result = result + chr(ord(data[i]) ^ ord(key[i % len(key)]))
    return str(base64.b64encode(bytes(result.encode())),'utf-8')

#Setting variables needed
username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = f'http://{username}.natas.labs.overthewire.org/'

print(f'The key found: {findingKey()}')
print(f'Cookie found: {xorEnc()}')

#The cookie found
cookies = 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'

#Connect to natas
session = requests.Session()
response = session.request('POST', url, auth=(username,password), cookies={'data':cookies})

#Filtering to get a password
#result = response.text
result = re.findall('The password for natas12 is (.*)<br>', response.text)[0]

print(result)
