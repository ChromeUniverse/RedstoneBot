# module imports
import asyncio
import aiohttp

# format function import
from format_list import format_list

from get_status import get_status

async def get_list(session, serverID, message):
  # getting status
  status, title, content = await get_status(session, serverID)

  # only attempt to get list when the server is ONLINE
  if status == 2:

    # building URLs
    console_command = 'https://ploudos.com/manage/' + serverID + '/console'
    console_get = 'https://ploudos.com/manage/' + serverID + '/console/refresh'

    # sending command to online console
    r_console_list = await session.post(console_command, data={'command': 'list'})
    await asyncio.sleep(1)

    # finding latest console log with online player list

    r_console_get = await session.get(console_get)
    html = await r_console_get.text()
    lines = html.split('\n')

    entry = ''
    for i in range(len(lines)-1, 0, -1):
      line = lines[i]
      if 'online' not in line:
        continue
      else:
        entry = line
        break

    # creating player list
    
    x = entry.find(':', 20)
    substring = entry[x+2:]
    players = substring.split(', ')
    print(players)
    
    await format_list(players, message, session, serverID)    

    message = ''

  # else, just send the title as the message
  else:
    message = title

  return message
