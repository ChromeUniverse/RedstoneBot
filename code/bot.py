# module imports
import asyncio
import aiohttp
import discord
from discord.ext import commands

# function imports from files
from login import login
from format_help import format_help
from get_status import get_status
from get_times import get_times
from activate import activate
from deactivate import deactivate
from reactivate import reactivate
from register import register

# database functions
from db_functions import (
    link,
    guild_in_db,
    IP_in_db,
    get_serverID,
)

# credentials
from credentials import (
    username,
    password,
    token,
)

# -----------------------------------------------------------------
# Discord setup
# -----------------------------------------------------------------



# command prefix
client = commands.Bot(command_prefix = '!redstone ')

# Redstone dust reddish color for Rich Embeds
redstoneRed = discord.Colour.from_rgb(221,55,55)

# removing default Help command
client.remove_command('help')

# bot startup
@client.event
async def on_ready():
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # logging in to ploudos.com
    login_status_code = await login(username, password, session)
    print('\nLogin status code: ' + str(login_status_code))

    print('Bot is ready to roll!\n')



# -----------------------------------------------------------------
# Discord commands
# -----------------------------------------------------------------


# help command - shows useful help page w/ commands + other things
@client.command()
async def help(ctx):

    title, content = format_help()
    # format and send rich embed
    page=discord.Embed(
        title=title,
        description=content,
        colour=redstoneRed
    )
    await ctx.send(embed=page)





# ping command - replies with "Pong!" + connection latency in miliseconds
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! :ping_pong: Connection latency is {round(client.latency * 1000)}ms')





# status command - displays server status
@client.command()
async def status(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # get server status
        status, title, content = await get_status(session, serverID)

        page=discord.Embed(
            title=title,
            description=content,
            colour=redstoneRed
        )
        await ctx.send(embed=page)





# queueTime command- displays queue waiting times
@client.command()
async def queueTime(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # get queue times
        title, content = await get_times(session, serverID)

        # format and send rich embed
        page=discord.Embed(
            title=title,
            description=content,
            colour=redstoneRed
        )
        await ctx.send(embed=page)





looping = False
# open command - activates the server
@client.command()
async def start(ctx, arg=None):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # checking for valid argument
        if arg == '1':
            message = 'Nuremberg selected.'
        elif arg == '2':
            message = 'St. Louis selected.'
        else:
            await ctx.send('You forgot to specify a valid location! The syntax for this command is: ```!redstone start [location]\n[location] = 1 🠖 Nuremberg, Germany\n[location] = 2 🠖 St. Louis, USA```')
            return None

        # message
        await ctx.send(message + ' Activating server... please wait.')

        global looping
        print("bot.py looping is..." + str(looping))

        if looping == False:
            looping = True
            # client.loop.create_task(activate(ctx, session))
            looping = await activate(ctx, session, serverID, arg)
        else:
            await ctx.send('Activation already in progress!')





# close command - deactivates the server
@client.command()
async def stop(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        await ctx.send('Closing server... please wait.')
        message = await deactivate(session, serverID)
        await ctx.send(message)




# start command - reactivates the server
@client.command()
async def restart(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        await ctx.send('Reactivating server... please wait.')
        message = await reactivate(session, serverID)
        await ctx.send(message)




@client.command()
async def setup(ctx, setupIP=None):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # getting Discord guild ('server') ID
    guildID = str(ctx.guild.id)
    # getting Discord guild ('server') name
    guildName = str(ctx.guild.name)
    # checking if member is a guild admin
    is_admin = ctx.author.guild_permissions.administrator

    # run registration
    title, content = await register(ctx, session, guildID, guildName, is_admin, setupIP)

    if title != None:
        # format and send rich embed
        page=discord.Embed(
            title=title,
            description=content,
            colour=redstoneRed
        )
        await ctx.send(embed=page)



# -----------------------------------------------------------------
# AsyncIO things
# -----------------------------------------------------------------

async def create_session(sess_list):
    # creates new aiohttp ClientSession
    new_sess = aiohttp.ClientSession()
    # adds new session to session list
    sess_list.append(new_sess)
    return new_sess

# storing aiohttp ClientSession in a list to make persistent sessions
# basically accessing a global variable
session_list = []

# main aynsc coroutine
async def main():
    # create new persistent aiohttp session
    session = await create_session(session_list)
    # client login + connect with token
    await client.start(token)

# running asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
