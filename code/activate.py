# module imports
import json
import requests
import asyncio

# importing status fetch function
from get_status import get_status

async def activate(ctx, session, serverID, arg):

    # stores server status from previous loop iteration
    # itialized as an invalid status (-1; see cheat sheet above)
    previous = -1

    while True:
        print("new loop iteration")

        # getting status
        status, title, content = await get_status(session, serverID)

        # only run activation when the server is OFFLINE
        if status == 0:
            print("let's enter the queue")

            # building queue url
            queue_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/queue/' + arg

            # performing GET request to queue_URl in order to enter the queue
            r_queue = session.get(queue_url)
            print(r_queue.text)

            # decoding JSON response text
            data = json.loads(r_queue.text)

            if not data["error"]:
                print('No errors')
                message = 'Activation sucessful! Check status with `!redstone status`.'
            else:
                message = 'Something went wrong! Please try again.'
                await ctx.send(message)
                break
            # sending message
            await ctx.send(message)

        # need to include sent_once = True / False here
        # for status == 3 and status == 4

        # if in queue
        elif status == 6:
            print("waiting in queue")
            message = title
            # sending message
            #await ctx.send(message)

        elif status == 7:
            print("let's confirm and activate the server")
            # building accept url
            accept_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/accept'

            # performing GET request to accept_url to start up
            r_accept = session.get(accept_url)
            print('accept status code: ' + str(r_accept.status_code))
            print('json response text: ' + str(r_accept.text))

            # decoding JSON response text
            data = json.loads(r_accept.text)
            print('json decoded')

            if not data["error"]:
                print('No errors')
                message = 'Confirmation successful! Server is starting up. Check status with `!redstone status`.'
            else:
                print('oppsie poopsie!')
                message = 'Something went wrong! Please try again.'
                await ctx.send(message)
                break
            # sending message
            await ctx.send(message)

        elif status == 2:
            print("Online!")

            # if going from 'start up' to 'online', then alert people
            if previous == 3:
                message = 'Server is up and running, @everyone! Check status with `!redstone status`.'
            else:
                message = 'Server is up and running!'

            # sending message
            await ctx.send(message)
            # breaking the loop
            return False
            break

        """

        # else, just send the title as the message
        else:
            message = title
            # sending message
            await ctx.send(message)
        """
        # setting previous state
        previous = status

        # async sleep for 2 seconds
        await asyncio.sleep(2)
