# module imports
import json
import aiohttp
import asyncio

# importing status fetch function
from get_status import get_status

# importing database function
from db_functions import get_looping

async def activate(ctx, session, serverID, arg, guildID):
    # stores server status from previous loop iteration
    # itialized as an invalid status (-1; see cheat sheet above)
    previous = -1

    while True:

        # get looping variable
        looping = get_looping(guildID)
        # looping was modified from outside the activation command
        if looping == 'False':
            # abort activation loop
            return False

        # only proceed if looping is True

        # getting status
        status, title, content = await get_status(session, serverID)

        # only run activation when the server is OFFLINE
        if status == 0:
            print("let's enter the queue")

            # building queue url
            queue_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/queue/' + arg

            # performing GET request to queue_URl in order to enter the queue
            r_queue = await session.get(queue_url)
            html = await r_queue.text()
            print(html)

            # decoding JSON response text
            data = json.loads(html)

            if not data["error"]:
                print('No errors')
                message = 'Activation successful! Check status with `!redstone status`.'
            else:
                message = 'Something went wrong! Please try again.'
                await ctx.channel.send(message)
                return False
                break
            # sending message
            await ctx.channel.send(message)

        # need to include sent_once = True / False here
        # for status == 3 and status == 4

        # if in queue
        elif status == 6:
            print("waiting in queue")
            message = title

        # if waiting for accept
        elif status == 7:
            print("let's confirm and activate the server")
            # building accept url
            accept_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/accept'

            # performing GET request to accept_url to start up
            r_accept = await session.get(accept_url)

            html = await r_accept.text()

            print('accept status code: ' + str(r_accept.status))
            print('json response text: ' + str(html))

            # decoding JSON response text
            data = json.loads(html)
            print('json decoded')

            if not data["error"]:
                print('Confirmation successful! Server is starting up')            
            else:
                print('oppsie poopsie!')
                message = 'Something went wrong! Please try again.'
                # sending message
                await ctx.channel.send(message)
                return False                
                break

        # if online
        elif status == 2:
            print("Online!")

            # if going from 'start up' to 'online', then alert people
            if previous == 3:
                message = 'Server is up and running, @everyone! Check status with `!redstone status`.'
            else:
                message = 'Server is up and running!'

            # sending message
            await ctx.channel.send(message)
            # breaking the loop
            return False
            break


        # setting previous state
        previous = status

        # async sleep for 2 seconds
        await asyncio.sleep(2)
