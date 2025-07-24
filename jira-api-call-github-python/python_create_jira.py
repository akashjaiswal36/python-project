# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://akashjaiswal-1746203677846.atlassian.net/rest/api/3/issue"

API_TOKEN = os.getenv("apitoken")

auth = HTTPBasicAuth("akashjaiswal@live.in", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "issuetype": {
      "id": "10036"
    },
    "project": {
      "key": "AK"
    },
    "summary": "First JIRA Ticket through API new laptop",
  },
  "update": {}
} )
  
response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))