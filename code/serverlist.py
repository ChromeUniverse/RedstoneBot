import json
import requests
from bs4 import BeautifulSoup

from urls import server_url

async def serverlist(session, setupIP):
    # Requesting data to internal internal API
    r_server = session.get(server_url)
    print('got server list')

    # using BS4 to parse the response
    src = r_server.content
    soup = BeautifulSoup(src, 'html.parser')

    things = soup.find_all(class_="menu")

    i = 1
    # looping through server entries on server list page
    #for i in range(len(things))
    while True:
        try:
            # parsing link to get serverIDs
            link = things[i].a['href']
            serverID = link[10:16]
            print('trying serverID: ' + serverID)

            # acessing internal API
            api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'
            r_api = session.get(api_endpoint)
            print('got API response ' + str(i))
            print(r_api.text)

            # decoding JSON response
            data = json.loads(r_api.text)
            print(data)

            # getting server IP address
            serverIP = data["serverIP"]
            serverName = data["serverName"]

            print('This is actual server IP: ' + serverIP)
            print('This is user input IP:    ' + setupIP)

            # comparing user input IP to actual IP
            if serverIP == setupIP:
                # if True, then we got a match!
                # return serverID for DB store
                print('Got it!')
                return serverID, serverName
            else:
                print('no dice\n\n')

            i += 1
        except:
            # couldn't find matching IP
            print('Done')
            return False, False
