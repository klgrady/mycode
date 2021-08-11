#!/usr/bin/python3

import requests

url='http://10.4.173.163:2224/check'

#post this data:
gwenp = {'answer': 'C'}

print(requests.post(url, data = gwenp).text)


