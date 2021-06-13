"""

    * REDSTONEBOT - Discord Bot for PloudOS servers *

Copyright (C) 2021 Lucca Rodrigues - All Rights Reserved

You may use, distribute and modify this code under the terms
of the GNU CPL v3.0 license. You should have received a copy 
of the license with this file and accompanying source code. 
If not, please visit:

https://github.com/ChromeUniverse/RedstoneBot/

"""


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
from get_list import get_list

# server member role functions
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
from bot_setup import (
  username,
  password,
  token,
  prefix,
  embedColor
)




# -----------------------------------------------------------------
# Discord bot setup
# -----------------------------------------------------------------



# Create Discord bot client 
client = discord.Client()

# Create color for Rich Embeds
embedColor = discord.Colour.from_rgb(embedColor[0], embedColor[1], embedColor[2])

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
# Discord commands handling
# -----------------------------------------------------------------



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # split message contents, get arguments

  args = message.content.split()

  if args[0] == prefix:

    # ping command
    if args[1] == 'ping':
        await message.channel.send(f'Pong! :ping_pong: Connection latency is {round(client.latency * 1000)}ms')

    # help command
    if args[1] == 'help':

      title, content = format_help()
      # format and send rich embed
      page=discord.Embed(
        title=title,
        description=content,
        colour=embedColor
      )

      await message.channel.send(embed=page)

    # status command 
    if args[1] == 'status':
      await status(message)

    # list command 
    if args[1] == 'list':
      await _list(message)

    # time command 
    if args[1] == 'time':
      await time(message)

    # start command 
    if args[1] == 'start':
      await start(message)

    # exit command 
    if args[1] == 'exit':
      await _exit(message)

    # stop command 
    if args[1] == 'stop':
      await stop(message)

    # restart command 
    if args[1] == 'restart':
      await restart(message)

    # setup command 
    if args[1] == 'setup':
      await setup(message)

    # reset command 
    if args[1] == 'reset':
      await reset(message)
  




# -----------------------------------------------------------------
# Discord command functions
# -----------------------------------------------------------------




# status command - displays server status
async def status(message):
  # retrieving aiohttp ClientSession
  global session_list
  session = session_list[0]

  # get server ID
  result = get_serverID(str(message.guild.id))

  if result == False:
    await message.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
    return 
  else:
    serverID = result

    # get server status
    status, title, content = await get_status(session, serverID)

    page=discord.Embed(
        title=title,
        description=content,
        colour=embedColor
    )
    await message.channel.send(embed=page)
    return 




# list command - shows list of online players
async def _list(message):
  # retrieving aiohttp ClientSession
  global session_list
  session = session_list[0]

  # get server ID
  result = get_serverID(str(message.guild.id))
  if result == False:
    await message.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
    return 
  else:
    serverID = result

    # get online player list
    msg = await get_list(session, serverID, message)      

    if msg != '':
      await(message.channel.send(msg))

    return
      


# time command- displays queue waiting times
async def time(message):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get server ID
    result = get_serverID(str(message.guild.id))
    if result == False:
        await message.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # get queue times
        title, content = await get_times(session, serverID)

        # format and send rich embed
        page=discord.Embed(
            title=title,
            description=content,
            colour=embedColor
        )
        await message.channel.send(embed=page)




# start command - activates the server
async def start(ctx):
    # retrieving aiohttp ClientSession
    global session_list
    session = session_list[0]

    # get discord guildID
    guildID = str(ctx.guild.id)

    # checking if member is a Redstone User
    if check_user(ctx) == False:
        await ctx.channel.send("Only designated Redstone Users can use this command.\nPlease ask your Discord server admin to give you the `Redstone User` role.")
        return None

    # get server ID
    result = get_serverID(guildID)
    if result == False:
        await ctx.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
        return None
    else:
        serverID = result

        # checking for valid argument
        try:
          arg = ctx.content.split()[2]
          if arg == '1':
            msg = 'Nuremberg selected.'
          else:
            raise Exception("Not a valid location!")
        
        except:
          msg = ''
          msg += 'Invalid location. The syntax for this command is:'
          msg += '```!redstone start [location]\n\n[location] = 1 🠖 Nuremberg, Germany```'

          await ctx.channel.send(msg)
          return

        # message
        await ctx.channel.send(msg + ' Activating server... please wait.')

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
            await ctx.channel.send('Activation already in progress!')


# exit command - leaves the queue
async def _exit(ctx):
  # getting the guildID
  guildID = str(ctx.guild.id)

  # retrieving aiohttp ClientSession
  global session_list
  session = session_list[0]

  # check if member is a Redstone/guild admin
  if check_admin(ctx) == False:
    await ctx.channel.send("Only members with the `Redstone Admin` role can use this command.\nThis is due to the fact that players sometimes have to wait *hours* before their server gets to the top of the PloudOS activation queue.")
    return None

  # get server ID
  result = get_serverID(str(ctx.guild.id))
  if result == False:
    await ctx.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
    return None
  else:
    serverID = result

    await ctx.channel.send('Exiting queue... please wait.')
    message = await leave_queue(session, serverID, guildID)
    await ctx.channel.send(message)



# stop command - deactivates the server
async def stop(ctx):
  # retrieving aiohttp ClientSession
  global session_list
  session = session_list[0]

  # checking if member is a Redstone User
  if check_user(ctx) == False:
    await ctx.channel.send("Only designated Redstone Users can use this command.\nPlease ask your Discord server admin to give you the `Redstone User` role.")
    return None

  # get server ID
  result = get_serverID(str(ctx.guild.id))
  if result == False:
    await ctx.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
    return None
  else:
    serverID = result

    # check if there are people online, if member has admin, stop the server
    message = await deactivate(session, serverID, ctx)
    await ctx.channel.send(message)



# restart command - reactivates the server
async def restart(ctx):
  # retrieving aiohttp ClientSession
  global session_list
  session = session_list[0]

  # checking if member is a Redstone User
  if check_user(ctx) == False:
    await ctx.channel.send("Only designated Redstone Users can use this command.\nPlease ask your Discord server admin to give you the `Redstone User` role.")
    return None

  # get server ID
  result = get_serverID(str(ctx.guild.id))
  if result == False:
    await ctx.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
    return None
  else:
    serverID = result

    await ctx.channel.send('Reactivating server... please wait.')
    message = await reactivate(session, serverID)
    await ctx.channel.send(message)



# links Discord server and PloudOS server
async def setup(ctx):
  # retrieving aiohttp ClientSession
  global session_list
  session = session_list[0]

  # getting Discord guild ('server') ID
  guildID = str(ctx.guild.id)
  # getting Discord guild ('server') name
  guildName = str(ctx.guild.name)
  # checking if member is a guild admin
  is_admin = check_admin(ctx)

  # run registration

  # checking for valid argument
  try:
    setupIP = ctx.content.split()[2]    
  
  except:
    msg = ''
    msg += 'Invalid location. The syntax for this command is:'
    msg += '```!redstone setup [IP address]\n\n[IP address] 🠖 mycoolserver.ploudos.me```'

    await ctx.channel.send(msg)
    return

  
  title, content = await register(ctx, session, guildID, guildName, is_admin, setupIP)

  if title != None:
    # format and send rich embed
    page=discord.Embed(
      title=title,
      description=content,
      colour=embedColor
    )
    await ctx.channel.send(embed=page)



# reset command - resets setup
async def reset(ctx):
  # get server ID
  result = get_serverID(str(ctx.guild.id))
  if result == False:
    await ctx.channel.send("This Discord server isn't linked to PloudOS yet. Use `!redstone setup [serverip]`.")
    return None
  else:
    serverID = result

    # getting Discord guild ('server') ID
    guildID = str(ctx.guild.id)
    # getting Discord guild ('server') name
    guildName = str(ctx.guild.name)
    # checking if member is a guild admin
    is_admin = check_admin(ctx)

    message = await unregister(guildID, guildName, is_admin)

    await ctx.channel.send(message)



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
