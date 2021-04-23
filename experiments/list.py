import json
import requests
import asyncio
import aiohttp
import datetime
import time

# credentials import
from credentials import (
    username,
    password,
)

serverID = 's30797'

# Important URLs
login_url = 'https://ploudos.com/login/'
api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'
console_command = 'https://ploudos.com/manage/' + serverID + '/console'
console_get = 'https://ploudos.com/manage/' + serverID + '/console/refresh'

# Initializing persistent sessions
# session = requests.Session()


# Payload with credentials
login_data = {
        'username': username,
        'password': password,
}

async def main():
  session = aiohttp.ClientSession()

  # Performing POST request to login + printing status code
  r_login = await session.post(login_url, data=login_data)
  print("\nStatus code: " + str(r_login.status) + '\n')

  # sending console command
  command = {
    'command': 'list'
  }

  r_console_list = await session.post(console_command, data=command)

  print('\nSent command at' + str(datetime.datetime.now()) + '\n')

  await asyncio.sleep(1)

  # getting console status

  r_console_get = await session.get(console_get)

  html = await r_console_get.text()

  lines = html.split('\n')
  print(lines)
  line = lines[len(lines)-2] 
  a = line.split(' ')
  # print(a)

  players = []
  for i in range(12, len(a)):
    player = a[i]
    if player[-1] == ',':
      player = player[:-1]

    players.append(player)

  print(players)

  print()
  await session.close()

asyncio.run(main())