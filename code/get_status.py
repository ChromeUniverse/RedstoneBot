# module imports
import json
import requests

# format function import
from format_status import format_status

async def get_status(session, serverID):
    # build API endpoint URL
    api_endpoint = 'https://ploudos.com/manage/s' + serverID + '/ajax2'

    # Requesting data to internal internal API
    r_status = session.get(api_endpoint)

    # check if we got some nonsense HTMl or a JSON
    if r_status.text[2] == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here
        print("Tried to access API, got nonsense HTML. *sigh*")

        return 'Something went wrong'

    else:
        # decoding JSON response text
        data = json.loads(r_status.text)
        print("Got the status JSON!")
        print(data)

        status, title, content = format_status(data)

        return status, title, content
