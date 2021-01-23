# module import
import requests

# args: Username, Password and Requests Session object
def login(username, password, session):
    login_url = 'https://ploudos.com/login/'

    # Payload with credentials
    data = {
            'username': username,
            'password': password,
    }

    # Performing POST request to login
    r_login = session.post(login_url, data=data)

    return r_login.status_code
