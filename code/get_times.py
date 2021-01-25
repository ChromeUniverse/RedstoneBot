# module imports
import json
import aiohttp
from bs4 import BeautifulSoup

# format function import
from format_queuetime import format_queuetime

async def get_times(session, serverID):
    # buuilding queue waiting time URL
    location_url = 'https://ploudos.com/manage/s' + serverID + '/ajax2/location'

    # Requesting data to internal  API
    r_times = await session.get(location_url)

    html = await r_times.text()

    # check if we got some nonsense HTMl or a JSON
    if html == '<':
        # very hacky solution, I know, I know :-\
        # the third char of the HTML template for the PloudOS.com sites is always a '<'
        # we'll use that to our advantage here
        print("Tried to access API, got nonsense HTML. *sigh*")

        return 'Something went wrong'

    else:
        # using BS4 to parse the response
        soup = BeautifulSoup(html, 'html.parser')

        # Nuremberg

        print("Here's the nuremberg_time:")

        things = soup.div.div.a.b.i.text

        timestr = []
        i = 42
        while True:
            newchar = things[i]
            if newchar != ' ':
                timestr.append(newchar)
                i += 1
            else:
                break

        nuremberg_time = ''.join(timestr)
        print(nuremberg_time)

        # St. Louis

        print("Here's the stlouis_time:")

        things = soup.div.div.i.i.i.div.div.a.text

        timestr = []
        i = 125
        while True:
            newchar = things[i]
            if newchar != ' ':
                timestr.append(newchar)
                i += 1
            else:
                break

        stlouis_time = ''.join(timestr)
        print(stlouis_time)

        title, content = format_queuetime(nuremberg_time, stlouis_time)
        return title, content
