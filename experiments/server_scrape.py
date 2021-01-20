import json
import requests
from bs4 import BeautifulSoup

# credentials import
from credentials import (
    username,
    password,
)

serverID = ''
# Important URLs
login_url = 'https://ploudos.com/login/'
api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'
server_url = 'https://ploudos.com/server'


# Initializing persistent sessions
session = requests.Session()

# Payload with credentials
data = {
        'username': username,
        'password': password,
}

# Performing POST request to login + printing status code
r_login = session.post(login_url, data=data)
print("\nStatus code: " + str(r_login.status_code) + '\n')

# Requesting data to internal internal API
r_server = session.get(server_url)

# using BS4 to parse the response
src = r_server.content
soup = BeautifulSoup(src, 'html.parser')

things = soup.find_all(class_="menu")

i = 1
while True:
    try:
        # parsing link to get serverID
        link = things[i].a['href']
        serverID = link[10:16]

        # acessing internal API
        api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'
        r_api = session.get(api_endpoint)

        # decoding JSON response
        data = json.loads(r_api.text)

        # getting server IP address
        serverIP = data["serverIP"]
        name = data["serverName"]

        print('Server number ' + str(i) + '\n\tName: ' + name + '\n\tServerID: ' + serverID +'\n\tIP: ' + serverIP)

        i += 1
    except:
        print('Done')
        break
