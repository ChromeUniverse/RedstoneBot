# module import
import aiohttp

# args: Username, Password and Requests Session object
async def login(username, password, session):
    # login url
    login_url = 'https://ploudos.com/login/'

    # Payload with credentials
    payload = {
            'username': username,
            'password': password,
    }

    # POST request to login url
    r_login = await session.post(login_url, data=payload)

    return r_login.status
