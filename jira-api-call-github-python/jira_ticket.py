from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json

# creating flask app instance
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():

    # GitHub sends JSON payload — parse it
    data = request.json

    # Extract info from GitHub issue (adjust keys as needed)
    github_title = data.get("issue", {}).get("title", "No Title Provided")
    github_body = data.get("comment", {}).get("body", "No Description Provided")

    url = "https://akashjaiswal-1746203677846.atlassian.net/rest/api/3/issue"

    API_TOKEN = ...

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
        "summary": github_title,
    },
    "update": {}
    } )

    if github_body == "/jira":
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

        print("githun_body:", github_body)
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        print("GitHub Body not '/jira'. Skipping JIRA creation.")
        return json.dumps({"message": "JIRA not created. Condition not met."}, indent=4)

app.run('0.0.0.0')
