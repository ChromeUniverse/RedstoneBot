import asyncio
import aiohttp

from credentials import (
    username,
    password,
    serverID
)

async def login(session):
    # login url
    login_url = 'https://ploudos.com/login/'

    # form data to be sent
    payload = {
        'username': username,
        'password': password,
    }

    # POST request to login url
    r_login = await session.post(login_url, data=payload)

    # printing status code
    print('Login Status Code: ' + str(r_login.status))

async def api_call(session):
    # api endpoint
    api_endpoint = 'http://ploudos.com/manage/' + serverID + '/ajax2'

    # GET request to API endpoint
    r_status = await session.get(api_endpoint)

    # printing status code
    print('Status code: ' + str(r_status.status))
    # printing text
    data = await r_status.text()
    print(data)


async def main():
    session = aiohttp.ClientSession()

    # make login first
    await login(session)
    # then call the API
    await api_call(session)
    # close ClientSession
    await session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
