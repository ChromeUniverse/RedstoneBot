# module imports
import asyncio
import json
import csv
import requests
import discord
from discord.ext import commands

# function imports
from login import login
from format_help import format_help
from serverlist import serverlist

from db_write import link
from db_read import guild_in_db, IP_in_db

from functions import (
    get_status,
    activate,
    deactivate,
    reactivate,
    get_times
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

# test
# arg -> server IP
@client.command()
async def setup(ctx, setupIP=None):

    # getting Discord guild ('server') ID
    guildID = str(ctx.guild.id)

    # member admin status bool
    is_admin = ctx.author.guild_permissions.administrator

    if is_admin == True:

        if type(setupIP) == str and '.ploudos.me' in setupIP:

            # check that server isn't already in DB
            if guild_in_db(guildID) == True:
                await ctx.send('This Discord server is already linked to a PloudOS server.')
                return None
            else:
                # check that IP isn't already in DB
                if IP_in_db(setupIP) == True:
                    await ctx.send('This PloudOS server is already linked to another Discord server.')
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

                        await ctx.send('Setup successful! "' + serverName + '" has been linked to this Discord server')


                    else:
                        # couldn't match user input IP and IPs on server list
                        await ctx.send('Incorrect server IP, try again.')

        else:
            # invalid argument!
            await ctx.send('Argument error!')
    else:
        # user doesn't have server admin
        await ctx.send('Only users with admin permissions can use this command.')

# running the Discord bot with the provided token
client.run(token)
