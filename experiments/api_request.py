import json
import requests

# credentials import
from credentials import (
    username,
    password,
)

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

# Performing POST request to login + printing status code
r_login = session.post(login_url, data=data)
print("\nStatus code: " + str(r_login.status_code) + '\n')

# Requesting data to internal internal API
r_status = session.get(api_endpoint)

# check if we got some nonsense HTMl or a JSON
if r_status.text[2] == '<':
    # very hacky solution, I know, I know :-\
    # the third char of the HTML template for the PloudOS.com sites is always a '<'
    # we'll use that to our advantage here

    print("Tried to access API, got nonsense HTML. *sigh*")
    print("Either RedstoneBot is broken or PloudOS is undergoing maintenance.")
    print("Please login to PloudOS.com and visit https://ploudos.com/server for details.")
    print("If you think this is RedstoneBot's fault, please visit github.com/ChromeUniverse/RedstoneBot and open an issue.")
else:
    # decoding JSON response text
    data = json.loads(r_status.text)

    print("Got the JSON data! Here it is: \n")

    for key in data:
        print(key + ": " + str(data[key]))
