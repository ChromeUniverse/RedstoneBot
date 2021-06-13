# module imports
import json
import aiohttp

# importing status fetch function
from get_status import get_status
from role_functions import (
    check_user,
    check_admin,
)
from online_player_count import online_player_count

async def deactivate(session, serverID, ctx):
    # getting status
    status, title, content = await get_status(session, serverID)

    # only run deactivation when the server is ONLINE
    if status == 2:

        # get the number of players connected to the server
        num_players = await online_player_count(session, serverID)

        # there might still be people online!
        if num_players > 0:

            # check if member is Redstone/Guild admin
            if check_admin(ctx) == False:
                # won't force close if member isn't admin
                message = "There are still players connected to the server, can't shut it down now!\nOnly members with the `Redstone Admin` role can force close servers."
                return message

        # if:
        # there isn't anyone online...
        # OR if:
        # the member is Redstone/Guild admin...
        # then just keep going!
        await ctx.channel.send('Closing server... please wait.')

        # building stop url
        stop_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/stop'

        # performing GET request to accept_url to start up
        r_stop = await session.get(stop_url)

        html = await r_stop.text()

        # decoding JSON response text
        data = json.loads(html)
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
