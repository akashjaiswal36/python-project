# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://akashjaiswal-1746203677846.atlassian.net/rest/api/3/project"

API_TOKEN= "ATATT3xFfGF0XAxuNms0D4n8HzQH8Iw7hFm0YWgF7tLO4agczBlI3MOWZK8iGDO4Yd6GcpwUm6yVPtkyVLqkgGRUaUrCtODooV05zRuD1ihZrgWGV49Dtb62UlecWf3yhfa3Q_neF7RSnpl2zZZT65NOKUNsUMEDL732M7Zj-bpOAITfVJwHors=4A2696BC"

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