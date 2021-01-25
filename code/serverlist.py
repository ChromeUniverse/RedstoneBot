# module imports
import json
import aiohttp
from bs4 import BeautifulSoup

# database function imports
from db_functions import (
    serverID_in_db,
    get_IP,
)

async def serverlist(session, setupIP):
    serverlist_url = 'https://ploudos.com/server/'
    # Requesting data to internal internal API
    r_server = await session.get(serverlist_url)
    print('got server list')

    # using BS4 to parse the response
    serverlist_html = await r_server.text()
    soup = BeautifulSoup(serverlist_html, 'html.parser')

    # list of servers on server list
    servers = soup.find_all(class_="menu")

    print(servers)

    # looping through server entries on server list page
    for i in range(1, len(servers)):
        # parsing link to get serverIDs
        link = servers[i].a['href']
        serverID = link[10:16]
        print('trying serverID: ' + serverID)

        # if someone hasn't registerd this server
        if serverID_in_db(serverID) == False:
            # get this server's IP address through API call
            api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'
            # get request to API
            r_api = await session.get(api_endpoint)

            # decode JSON response
            api_html = await r_api.text()
            data = json.loads(api_html)
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
                print("Didn't work.\n\n")
        else:
            # found server ID in database
            print('Server already registered.\n\n')

    # couldn't find matching IP
    print("Couldn't find IP in serverlist")
    return False, False
