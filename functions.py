import json

from format import format

from urls import (
    login_url,
    api_endpoint,
    location_url,
    queue_url,
    accept_url,
    start_url,
    stop_url,
)

async def get_status(session):
    # Requesting data to internal internal API
    r_status = session.get(api_endpoint)
    # check if we got some nonsense HTMl or a JSON
    if r_status.text[2] == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here

        print("Tried to access API, got nonsense HTML. *sigh*")
        print("Either RedstoneBot is broken or PloudOS is undergoing maintenance.")
        print("Please login to PloudOS.com and visit https://ploudos.com/server for details.")
        print("If you think this is RedstoneBot's fault, please visit github.com/ChromeUniverse/RedstoneBot and open an issue.")

        return 'Something went wrong'

    else:
        # decoding JSON response text
        data = json.loads(r_status.text)

        print("Got the JSON data! Here it is: \n")

        for key in data:
            print(key + ": " + str(data[key]))

        title, content = format(data)

        return title, content

async def activate(session):
    r_queue = session.get(queue_url + '1')
    print(r_queue.text)

    message = 'Server activation in progress! Check server status with `!redstone status`.'
    return message

async def confirm(session):
    r_accept = session.get(accept_url)
    print(r_accept.text)

    message = 'Confirmation sent! Check server status with `!redstone status`.'
    return message

async def deactivate(session):
    r_stop = session.get(stop_url)
    print(r_stop.text)

    message = 'Server deactivation in progress! Check server status with `!redstone status`.'
    return message

async def reactivate(session):
    r_start = session.get(start_url)
    print(r_start.text)

    message = 'Server reactivation in progress! Check server status with `!redstone status`.'
    return message
