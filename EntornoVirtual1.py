import requests
r= requests.get('http://info.cern.ch/')
print(r.status_code)
print(r.text)
#print(r.json())