import requests
from urls import login_url

# login to PloudOS.com

# args: Username, Password and Requests Session object
def login(username, password, session):

    # Payload with credentials
    data = {
            'username': username,
            'password': password,
    }

    # Performing POST request to login
    r_login = session.post(login_url, data=data)

    return r_login.status_code
