# This is RedstoneBot's source code!

import json
import requests
import time
import discord
from discord.ext import commands


# Replace these with your actual PloudOS credentials
username = 'username'
password = 'password'

# Enter your secret bot token here!
token = 'bot_token_goes_here'

# Enter your ServerID here!
serverID = 's00000'


# Important URLs!

# Login page
login_url = 'https://ploudos.com/login/'

# Internal API endpoint URL
api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'

# Server locations
location_url = api_endpoint + '/location'

# Queue
choice = '0'
queue_url = api_endpoint + '/queue/'

# Accept
accept_url = api_endpoint + '/accept'

# Start
start_url = api_endpoint + '/start'

# Stop
stop_url = api_endpoint + '/stop'


# Initializing persistent sessions
session = requests.Session()

# login to PloudOS.com
def login():

    # Payload with credentials
    data = {
            'username': username,
            'password': password,
    }

    # Performing POST request to login + printing status code
    r_login = session.post(login_url, data=data)

    return r_login.status_code

# format Rich Embed message

def format(data):

    status = ''
    message = '\n'
    message += 'Server name: **' + str(data["serverName"]) + '**'
    message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    if data["status"] == 'READY':

        message += '\n\n**Server Resources**\n'
        message += '\nCPU: **' + str(data["serverUsedCPU"]) + '%** in use'
        message += '\nMemory: **' + str(data["serverUsedRAM"]) + ' MB** in use out of **' + str(data["serverMaxRam"]) + ' MB** max'
        message += '\nSSD storage: **' + str(data["serverUsedSpace"]/1000) + ' GB** used out of **' + str(data["serverTotalSpace"]/1000) + ' GB** max'
        message += '\n\n**Extra Info**\n'


        if data["isRunning"] == False:

            message = '\n'
            message += 'Server name: **' + str(data["serverName"]) + '**'
            message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

            if data["isEditorMode"] == True:
                # actually means that the Server is offline!
                status = 'Server is offline.'

            if data["isEditorMode"] == False:
                status = 'Server stopped.'
                message += '\nTimeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'


        if data["isRunning"] == True:
            if data["isStarted"] == True:
                status = 'Server is up and running!'
                message += '\nPlayers online: **' + str(data["onlineCount"]) + '** out of **' + str(data["onlineMax"]) + '** max'
                message += '\nTimeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'

            if data["isStarted"] == False:
                status = 'Server is starting up!'



    elif data["status"] == "SETUP":

        status = 'Server is running setup!'


    elif data["status"] == "CLOSING":

        status = 'Server is closing'


    elif data["status"] == "OFFLINE":

        status = 'Server is offline.'


    elif data["status"] == "QUEUE":

        status = 'Server is in the queue!'

        message += '\n\n**Queue Info**\n'
        message += '\nQueue position: **' + str(data["queuePos"]) +'** out of **'+ str(data["queuePos"]) + '**'
        message += '\nApproximate waiting time: **' + str(data["queueTimeFormatted"]) + ' minute(s)**'

    elif data["status"] == "WAITING_FOR_ACCEPT":

        status = 'Waiting for user confirmation on admin page.'

        message += '\n\n**Use the `!redstone accept` command!**\n'

    return status, message


# -----------------------------------------------------------------
# main async function definitions
# -----------------------------------------------------------------


async def get_status():
    # Requesting data to internal internal API
    r_status = session.get(api_endpoint)
    # check if we got some nonsense HTMl or a JSON
    if r_status.text[2] == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here

        print("Tried to access API, got nonsense HTML. *sigh*")
        print("Either RedstoneBot is broken or PloudOS is undergoing maintenance.")
        print("Please login to PloudOS.com and visit https://ploudos.com/server for details.")
        print("If you think this is RedstoneBot's fault, please visit github.com/ChromeUniverse/RedstoneBot and open an issue.")

        return 'Something went wrong'

    else:
        # decoding JSON response text
        data = json.loads(r_status.text)

        print("Got the JSON data! Here it is: \n")

        for key in data:
            print(key + ": " + str(data[key]))

        title, content = format(data)

        return title, content

async def activate():

    """
    r_location = session.get(location_url)
    print(r_location.text)
    """

    r_queue = session.get(queue_url + '1')
    print(r_queue.text)

    message = 'Server activation in progress! Check server status with `!redstone status`.'
    return message

async def confirm():
    r_accept = session.get(accept_url)
    print(r_accept.text)

    message = 'Confirmation sent! Check server status with `!redstone status`.'
    return message

async def deactivate():
    r_stop = session.get(stop_url)
    print(r_stop.text)

    message = 'Server deactivation in progress! Check server status with `!redstone status`.'
    return message

async def reactivate():
    r_start = session.get(start_url)
    print(r_start.text)

    message = 'Server reactivation in progress! Check server status with `!redstone status`.'
    return message









# -----------------------------------------------------------------
# Discord stuff
# -----------------------------------------------------------------


# command prefix
client = commands.Bot(command_prefix = '!redstone ')

# bot startup
@client.event
async def on_ready():
    print('Login status code: ' + str(login()))
    print('Bot is ready.')

# ping command - replies with "Pong!" + connection latency in miliseconds
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! :ping_pong: Connection latency is {round(client.latency * 1000)}ms')

# status command - displays server status
@client.command()
async def status(ctx):
    #start = time.time()

    # get server status
    title, content = await get_status()

    # format and send rich embed
    page1=discord.Embed(
        title=title,
        description=content,
        colour=discord.Colour.from_rgb(221,55,55)
    )
    await ctx.send(embed=page1)

    #end = time.time()

    # send time elapsed message
    #await ctx.send(f'\n\nServer status fetching took ~**{round(end - start + client.latency)} seconds**.')

opening = False

# open command - activates the server
@client.command()
async def open(ctx):
    await ctx.send('Activating server... please wait.')
    message = await activate()
    await ctx.send(message)

# accept command - confirmation
@client.command()
async def accept(ctx):
    await ctx.send('Sending confirmation... please wait.')
    message = await confirm()
    await ctx.send(message)

# start command - reactivates the server
@client.command()
async def start(ctx):
    await ctx.send('Reactivating server... please wait.')
    message = await reactivate()
    await ctx.send(message)

# close command - deactivates the server
@client.command()
async def stop(ctx):
    await ctx.send('Closing server... please wait.')
    message = await deactivate()
    await ctx.send(message)

"""
# info command - returns useful server info
@client.command()
async def info(ctx):
    await ctx.send('Getting server info... please wait.')
    start = time.time()
    message = get_info()
    print(message)
    page1=discord.Embed(
        title=status,
        description=message,
        colour=discord.Colour.from_rgb(221,55,55)
    )
    await ctx.send(embed=page1)
    end = time.time()
    await ctx.send(f'\n\nServer info fetching took ~**{round(end - start + client.latency)} seconds**.')
"""
# running the Discord bot with the provided token
client.run(token)
