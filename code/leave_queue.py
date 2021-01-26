# module imports
import json
import aiohttp

# importing status fetch function
from get_status import get_status

# import database function
from db_functions import update_looping

async def leave_queue(session, serverID, guildID):
    # getting status
    status, title, content = await get_status(session, serverID)

    # only run activation when the server is IN QUEUE
    if status == 6:

        # update looping in database
        # immediately stops actiavtion loop!
        update_looping(guildID, False)

        # building stop url
        exit_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/exitQueue'

        # performing GET request to accept_url to start up
        r_exit = await session.get(exit_url)

        html = await r_exit.text()

        # decoding JSON response text
        data = json.loads(html)
        print(data)

        if not data["error"]:
            print('No errors')
            message = 'Successfully left the queue. Check status with `!redstone status`.'

        else:
            message = 'Something went wrong! Please try again.'
            return message

    # else, just send the title as the message
    else:
        message = title

    return message
