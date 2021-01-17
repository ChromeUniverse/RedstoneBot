import time
import json
import requests
from format import format

# credentials import
from credentials import (
    username,
    password,
)

# Login page
login_url = 'https://ploudos.com/login/'

# Internal API endpoint URL
api_endpoint = 'https://ploudos.com/manage/' + serverID + '/ajax2'

# Server locations
location_url = api_endpoint + '/location'

# Queue
queue_url = api_endpoint + '/queue/'

# Accept
accept_url = api_endpoint + '/accept'

# Start
start_url = api_endpoint + '/start'

# Stop
stop_url = api_endpoint + '/stop'

# Initializing persistent sessions
session = requests.Session()

# Payload with credentials
data = {
        'username': username,
        'password': password,
}

# Performing POST request to login + printing status code
r_login = session.post(login_url, data=data)
print("\nStatus code: " + str(r_login.status_code) + '\n')


# status cheat sheet
#
# 0 -> offline
# 1 -> stopped execution
# 2 -> up and running
# 3 -> starting up
# 4 -> running setup
# 5 -> closing
# 6 -> in queue
# 7 -> waiting for accept
#

# program flow:
#   if 0    -> start server
#   if 6    -> keep requesting
#   if 7    -> confirm
#   else    -> HALT

while True:
    # Requesting data to internal internal API
    r_status = session.get(api_endpoint)

    # decoding JSON
    data = json.loads(r_status.text)

    # formatting and getting status
    status, title, content = format(data)
    print(status)

    if status == 0:
        print("let's enter the queue")

        # performing GET request to queue_URl in order to enter the queue
        r_queue = session.get(queue_url + '1')
        print(r_queue.text)

        # decoding JSON response text
        data = json.loads(r_queue.text)
        print(data)

        if not data["error"]:
            print('No errors')
            message = 'Server activation sucessful! Check status with `!redstone status`.'
        else:
            message = 'Something went wrong! Please try again.'
            break

    elif status == 6:
        print("waiting in queue")
        print(content)

    elif status == 7:
        print("let's confirm and activate the server ")

        # performing GET request to accept_url to start up
        r_accept = session.get(accept_url)
        print(r_accept.text)

        # decoding JSON response text
        data = json.loads(r_accept.text)
        print(data)

        if not data["error"]:
            print('No errors')
            message = 'Confirmation sucessful! Server is starting up. Check status with `!redstone status`.'
        else:
            message = 'Something went wrong! Please try again.'

    else:
        print("done")
        break

    # run every second
    time.sleep(1)
