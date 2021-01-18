import json
import requests
from bs4 import BeautifulSoup

# credentials import
from credentials import (
    username,
    password,
    serverID
)

# Important URLs
login_url = 'https://ploudos.com/login/'
queuetime_url = 'https://ploudos.com/manage/' + serverID + '/ajax2/location'

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
r_queue = session.get(queuetime_url)

# check if we got some nonsense HTMl or a JSON
if r_queue.text[2] == '<':
    # very hacky solution, I know, I know :-\
    # the third char of the HTML template for the PloudOS.com sites is always a '<'
    # we'll use that to our advantage here

    print("Tried to access API, got nonsense HTML. *sigh*")
    print("Either RedstoneBot is broken or PloudOS is undergoing maintenance.")
    print("Please login to PloudOS.com and visit https://ploudos.com/server for details.")
    print("If you think this is RedstoneBot's fault, please visit github.com/ChromeUniverse/RedstoneBot and open an issue.")
else:
    # using BS4 to parse the response
    src = r_queue.content
    soup = BeautifulSoup(src, 'html.parser')

    # Nuremberg

    print("Here's the nuremberg_time:")

    things = soup.div.div.a.b.i.text

    timestr = []
    i = 42
    while True:
        newchar = things[i]
        if newchar != ' ':
            timestr.append(newchar)
            i += 1
        else:
            break

    nuremberg_time = ''.join(timestr)
    print(nuremberg_time)

    # St. Louis

    print("Here's the stlouis_time:")

    things = soup.div.div.i.i.i.div.div.a.text

    timestr = []
    i = 125
    while True:
        newchar = things[i]
        if newchar != ' ':
            timestr.append(newchar)
            i += 1
        else:
            break

    stlouis_time = ''.join(timestr)
    print(stlouis_time)
