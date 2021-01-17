import json
import asyncio

from format import format

from urls import (
    login_url,
    api_endpoint,
    location_url,
    queue_url,
    accept_url,
    start_url,
    stop_url,
)

# status cheat sheet
#
# 0 -> offline                  *
# 1 -> stopped execution
# 2 -> online                   *
# 3 -> starting up
# 4 -> running setup
# 5 -> closing
# 6 -> in queue                 *
# 7 -> waiting for accept
# 8 -> preparing server reallocation

async def get_status(session):
    # Requesting data to internal internal API
    r_status = session.get(api_endpoint)
    # check if we got some nonsense HTMl or a JSON
    if r_status.text[2] == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here
        print("Tried to access API, got nonsense HTML. *sigh*")

        return 'Something went wrong'

    else:
        # decoding JSON response text
        data = json.loads(r_status.text)
        print("Got the JSON!")

        status, title, content = format(data)

        return status, title, content

async def activate(ctx, session):

    # stores server status from previous loop iteration
    # itialized as an invalid status (-1; see cheat sheet above)
    previous = -1

    while True:
        print("new loop iteration")

        # getting status
        status, title, content = await get_status(session)


        # only run activation when the server is OFFLINE
        if status == 0:
            print("let's enter the queue")

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
                break
            # sending message
            await ctx.send(message)

        # need to include sent_once = True / False here
        # for status == 3 and status == 4

        # if in queue
        elif status == 6:
            print("waiting in queue")
            message = title
            print(content)
            # sending message
            #await ctx.send(message)

        elif status == 7:
            print("let's confirm and activate the server")

            # performing GET request to accept_url to start up
            r_accept = session.get(accept_url)
            print(r_accept.status_code)

            # decoding JSON response text
            data = json.loads(r_accept.text)

            if not data["error"]:
                print('No errors')
                message = 'Confirmation sucessful! Server is starting up. Check status with `!redstone status`.'
            else:
                message = 'Something went wrong! Please try again.'
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


async def deactivate(session):

    # getting status
    status, title, content = await get_status(session)

    # only run activation when the server is ONLINE
    if status == 2:

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

async def reactivate(session):
    # getting status
    status, title, content = await get_status(session)

    # only run activation when the server is STOPPED
    if status == 1:

        # performing GET request to accept_url to start up
        r_start = session.get(start_url)
        print(r_start.text)

        # decoding JSON response text
        data = json.loads(r_start.text)
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
