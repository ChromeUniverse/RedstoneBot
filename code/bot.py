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
from leave_queue import leave_queue
from unregister import unregister

# member role functions
from role_functions import (
    check_user,
    check_admin,
)

# database functions
from db_functions import (
    link,
    guild_in_db,
    IP_in_db,
    get_serverID,
    get_looping,
    update_looping,
    deleteEntry,
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






# open command - activates the server
@client.command()
async def start(ctx, arg=None):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get discord guildID
    guildID = str(ctx.guild.id)

    # checking if member is a Redstone User
    if check_user(ctx) == False:
        await ctx.send("Only designated Redstone Users can use this command.\nPlease ask your Discord server admin to give you the `Redstone User` role.")
        return None

    # get server ID
    result = get_serverID(guildID)
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
            message = ''
            message += 'Invalid location. The syntax for this command is:'
            message += '```!redstone start [location]\n\n[location] = 1 🠖 Nuremberg, Germany\n[location] = 2 🠖 St. Louis, USA```'

            await ctx.send(message)
            return None

        # message
        await ctx.send(message + ' Activating server... please wait.')

        # get looping status for this Guild
        looping = get_looping(guildID)
        print("bot.py looping is..." + str(looping))

        # yep, string, not boolean
        if looping == 'False':
            looping = True
            update_looping(guildID, looping)

            # start server activatation loop
            looping = await activate(ctx, session, serverID, arg, guildID)
            update_looping(guildID, looping)
        else:
            await ctx.send('Activation already in progress!')


# exit command - leaves the queue
@client.command()
async def exit(ctx):
    # getting the guildID
    guildID = str(ctx.guild.id)

    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # check if member is a Redstone/guild admin
    if check_admin(ctx) == False:
        await ctx.send("Only members with the `Redstone Admin` role can use this command.\nThis is due to the fact that players sometimes have to wait *hours* before their server gets to the top of the PloudOS activation queue.")
        return None

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        await ctx.send('Exiting queue... please wait.')
        message = await leave_queue(session, serverID, guildID)
        await ctx.send(message)




# close command - deactivates the server
@client.command()
async def stop(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # checking if member is a Redstone User
    if check_user(ctx) == False:
        await ctx.send("Only designated Redstone Users can use this command.\nPlease ask your Discord server admin to give you the `Redstone User` role.")
        return None

    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # check if there are people online, if member has admin, stop the server
        message = await deactivate(session, serverID, ctx)
        await ctx.send(message)




# start command - reactivates the server
@client.command()
async def restart(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # checking if member is a Redstone User
    if check_user(ctx) == False:
        await ctx.send("Only designated Redstone Users can use this command.\nPlease ask your Discord server admin to give you the `Redstone User` role.")
        return None

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




# links Discord server and PloudOS server
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


# reset command - resets setup
@client.command()
async def reset(ctx):
    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # getting Discord guild ('server') ID
        guildID = str(ctx.guild.id)
        # getting Discord guild ('server') name
        guildName = str(ctx.guild.name)
        # checking if member is a guild admin
        is_admin = ctx.author.guild_permissions.administrator

        message = await unregister(guildID, guildName, is_admin)

        await ctx.send(message)



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
