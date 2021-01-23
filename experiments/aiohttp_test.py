import asyncio
import aiofiles
import aiohttp

"""
async def main():
    url = 'https://www.boxofficemojo.com/year/2019'
    async with ClientSession() as session:
        async with session.get(url) as response:
            html_body = await response.read()
            return html_body
"""

#print(asyncio.run(main()))


async def fetch(url, session):
    response = await session.get(url)
    print('Status code: ' + str(response.status))
    html = await response.text()
    return html

async def write_to_file(file, text):
    async with aiofiles.open(file, 'w') as f:
        await f.write(text)

async def main(urls):
    session = aiohttp.ClientSession()
    tasks = []
    for url in urls:
        file = f'{url.split("//")[-1]}.txt'
        html = await fetch(url, session)
        tasks.append(write_to_file(file, html))

    await session.close()
    await asyncio.gather(*tasks)

urls = ['http://example.com']

asyncio.run(main(urls))
