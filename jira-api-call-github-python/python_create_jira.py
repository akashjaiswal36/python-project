# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://akashjaiswal-1746203677846.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0XAxuNms0D4n8HzQH8Iw7hFm0YWgF7tLO4agczBlI3MOWZK8iGDO4Yd6GcpwUm6yVPtkyVLqkgGRUaUrCtODooV05zRuD1ihZrgWGV49Dtb62UlecWf3yhfa3Q_neF7RSnpl2zZZT65NOKUNsUMEDL732M7Zj-bpOAITfVJwHors=4A2696BCs"

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
    "summary": "First JIRA Ticket through API",
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