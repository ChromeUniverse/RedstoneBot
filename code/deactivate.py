# module imports
import json
import requests

# importing status fetch function
from get_status import get_status

async def deactivate(session, serverID):
    # getting status
    status, title, content = await get_status(session, serverID)

    # only run activation when the server is ONLINE
    if status == 2:
        # building stop url
        stop_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/stop'

        # performing GET request to accept_url to start up
        r_stop = session.get(stop_url)
        print(r_stop.text)

        # decoding JSON response text
        data = json.loads(r_stop.text)
        print(data)

        if not data["error"]:
            print('No errors')
            message = 'Server halted! Check status with `!redstone status`.'
        else:
            message = 'Something went wrong! Please try again.'

    # else, just send the title as the message
    else:
        message = title

    return message
