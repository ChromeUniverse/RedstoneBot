# module imports
import json
import aiohttp

# format function import
from format_status import format_status

async def get_status(session, serverID):
    # build API endpoint URL
    api_endpoint = 'https://ploudos.com/manage/s' + serverID + '/ajax2'

    # Requesting data to internal internal API
    r_status = await session.get(api_endpoint)

    data = await r_status.text()

    # check if we got some nonsense HTMl or a JSON
    if data[2] == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here
        print("Tried to access API, got nonsense HTML. *sigh*")

        # according to statusCheatSheet
        status = 10

        title = "Something went wrong. That ain't good."

        content = ''
        content += "Either PloudOS is in maintenance mode or Redstone is broken.\n\n "
        content += "Please visit https://ploudos.com/server/ to see if PloudOS is undergoing maintenance. \n\n"
        content += "If you think this is Redstone's fault, then please open a new issue at https://github.com/ChromeUniverse/RedstoneBot."


    else:
        # decoding JSON response text
        status_json = json.loads(str(data))
        print("Got the status JSON!")
        print(status_json)

        # formatting Rich Embed
        status, title, content = format_status(status_json)

    return status, title, content
