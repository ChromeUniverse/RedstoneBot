# module imports
import asyncio
import json
import requests
import discord
from discord.ext import commands

# function imports
from login import login

from functions import (
    get_status,
    activate,
    deactivate,
    reactivate,
)

# credentials import
from credentials import (
    username,
    password,
    token,
)


# Initializing persistent sessions
session = requests.Session()


# -----------------------------------------------------------------
# Discord commands
# -----------------------------------------------------------------


# command prefix
client = commands.Bot(command_prefix = '!redstone ')

# bot startup
@client.event
async def on_ready():
    print('Login status code: ' + str(login(username, password, session)))
    print('Bot is ready.')

# ping command - replies with "Pong!" + connection latency in miliseconds
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! :ping_pong: Connection latency is {round(client.latency * 1000)}ms')

# status command - displays server status
@client.command()
async def status(ctx):
    # get server status
    status, title, content = await get_status(session)

    # format and send rich embed
    page1=discord.Embed(
        title=title,
        description=content,
        colour=discord.Colour.from_rgb(221,55,55)
    )
    await ctx.send(embed=page1)

looping = False
# open command - activates the server
@client.command()
async def start(ctx):
    await ctx.send('Activating server... please wait.')

    global looping
    print("bot.py looping is..." + str(looping))

    if looping == False:
        looping = True
        # client.loop.create_task(activate(ctx, session))
        looping = await activate(ctx, session)
    else:
        await ctx.send('Activation already in progress!')

# start command - reactivates the server
@client.command()
async def restart(ctx):
    await ctx.send('Reactivating server... please wait.')
    message = await reactivate(session)
    await ctx.send(message)

# close command - deactivates the server
@client.command()
async def stop(ctx):
    await ctx.send('Closing server... please wait.')
    message = await deactivate(session)
    await ctx.send(message)


# running the Discord bot with the provided token
client.run(token)
