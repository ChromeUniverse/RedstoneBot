# module imports
import json
import asyncio
from bs4 import BeautifulSoup

# formmating functions
from format_status import format_status
from format_queuetime import format_queuetime

# getting urls
from urls import (
    login_url,
    api_endpoint,
    location_url,
    queue_url,
    accept_url,
    start_url,
    stop_url,
)

# database functions
from db_functions import (
    link,
    guild_in_db,
    IP_in_db,
)

from serverlist import serverlist

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

async def get_status(session, serverID):
    # build API endpoint URL
    api_endpoint = 'https://ploudos.com/manage/s' + serverID + '/ajax2'

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

        status, title, content = format_status(data)

        return status, title, content

async def get_times(session, serverID):
    # buuilding queue waiting time URL
    location_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/location'

    # Requesting data to internal  API
    r_times = session.get(location_url)

    # check if we got some nonsense HTMl or a JSON
    if r_times.text[2] == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here
        print("Tried to access API, got nonsense HTML. *sigh*")

        return 'Something went wrong'

    else:
        # using BS4 to parse the response
        src = r_times.content
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

        title, content = format_queuetime(nuremberg_time, stlouis_time)
        return title, content


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
            print(content)
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

async def reactivate(session, serverID):
    # getting status
    status, title, content = await get_status(session, serverID)

    # only run activation when the server is STOPPED
    if status == 1:
        # building restart url
        start_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/start'

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

async def register(ctx, session, guildID, is_admin, setupIP):

    # check if member is admin
    if is_admin == True:

        # checking for valid argument
        if type(setupIP) == str and '.ploudos.me' in setupIP:

            # check that server isn't already in DB
            if guild_in_db(guildID) == True:
                await ctx.send('This Discord server is already linked to a PloudOS server.')
                return None
            else:
                # check that IP isn't already in DB
                if IP_in_db(setupIP) == True:
                    await ctx.send('This server IP is already linked to another Discord server.')
                    return None
                else:
                    # Got valid argument
                    await ctx.send("Running setup... please wait.")

                    # looping through online server list to get serverID
                    return1, return2 = await serverlist(session, setupIP)

                    if return1 != False:
                        #await ctx.send('Got valid IP!')
                        # managed to match input IP to actual IP on server list
                        serverID, serverName = return1, return2

                        # write data to DB
                        link(guildID, setupIP, serverID)

                        await ctx.send('Setup successful! **' + serverName + '** has been linked to this Discord server.')

                    else:
                        # couldn't match user input IP and IPs on server list
                        await ctx.send('Incorrect server IP, try again.')
        else:
            # invalid argument!
            await ctx.send('Argument error!')
    else:
        # user doesn't have server admin
        await ctx.send('Only users with admin permissions can use this command.')
