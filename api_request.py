import requests

# Credentials
username = "username"
password = "password"
serverID = "serverID"

# Important URLs
login_url = 'https://ploudos.com/login/'
api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'

# Initializing persistent sessions
session = requests.Session()

# Payload with credentials
data = {
        'username': username,
        'password': password,
}

# Preforming POST request to login + printing status code
r_login = session.post(login_url, data=data)
print("\nStatus code: " + str(r_login.status_code))

# Requesting data to internal internal API
r_status = session.get(api_endpoint)
print(r_status.text)

"""
Expecting the following response (or similar):
{"serverName":"Server Name","serverIP":"serverip.ploudos.me","serverVersion":"PaperSpigot 1.16.3","versionSupportUsage":true,"status":"OFFLINE","isInfinity":false,"skip":false}
"""
