# module imports
import requests
import discord
from discord.ext import commands

# function imports
from login import login
from format_help import format_help
from functions import (
    get_status,
    get_times,
    activate,
    deactivate,
    reactivate,
    register,
)

# database functions
from db_functions import (
    link,
    guild_in_db,
    IP_in_db,
    get_serverID,
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

# Redstone Red color for Rich Embeds
redstoneRed = discord.Colour.from_rgb(221,55,55)

# bot startup
@client.event
async def on_ready():
    print('Login status code: ' + str(login(username, password, session)))
    print('Bot is ready.')


client.remove_command('help')
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
    # get server ID
    result = get_serverID(str(ctx.guild.id))
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # get server status
        status, title, content = await get_status(session, serverID)

        # format and send rich embed
        page=discord.Embed(
            title=title,
            description=content,
            colour=redstoneRed
        )
        await ctx.send(embed=page)

# queueTime command- displays queue waiting times
@client.command()
async def queueTime(ctx):
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

# start command - reactivates the server
@client.command()
async def restart(ctx):
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

# close command - deactivates the server
@client.command()
async def stop(ctx):
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

@client.command()
async def setup(ctx, setupIP=None):
    # getting Discord guild ('server') ID
    guildID = str(ctx.guild.id)
    # member admin status bool
    is_admin = ctx.author.guild_permissions.administrator

    # run registration
    await register(ctx, session, guildID, is_admin, setupIP)


# running the Discord bot with the provided token
client.run(token)
