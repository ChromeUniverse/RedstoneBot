# module imports
import json
import aiohttp
import requests

# importing status fetch function
from get_status import get_status

async def reactivate(session, serverID):
    # getting status
    status, title, content = await get_status(session, serverID)

    # only run activation when the server is STOPPED
    if status == 1:
        # building restart url
        start_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/start'

        # performing GET request to accept_url to start up
        r_start = await session.get(start_url)

        html = await r_start.text()

        # decoding JSON response text
        data = json.loads(html)
        print(data)

        if not data['error']:
            print('No errors')
            message = 'Reactivation sucessful! Server is starting up. Check status with `!redstone status`.'
        else:
            message = 'Something went wrong! Please try again.'

    # else, just send the title as the message
    else:
        message = title

    return message
