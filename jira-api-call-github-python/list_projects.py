# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://akashjaiswal-1746203677846.atlassian.net/rest/api/3/project"

API_TOKEN = os.getenv("apitoken") 

auth = HTTPBasicAuth("akashjaiswal@live.in", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
for i in (range(len(output))):
  print(output[i]["name"])