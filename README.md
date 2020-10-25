# RedstoneBot

**Redstone** is a Discord bot built for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/), originally built for the SMP BR community.

This bot was built with [Python 3](http://python.org/), [Selenium for Python](https://selenium-python.readthedocs.io/#), [JSON](https://docs.python.org/3/library/json.html) and [Discord.py](https://github.com/Rapptz/discord.py)

![image](https://i.imgur.com/PcRwByp.png)


## Working commands

* `!redstone ping` Replies with "Pong!" and show connection latency in miliseconds
* `!redstone status` Shows current server status: "Online", "In queue", "Starting up", etc., along with additional info about server resources, number of online players, and more (see picure above for example)

## To-do

* Migrate from Selenium to [Requests](https://requests.readthedocs.io/en/master/)
* Commands to add:
  * `!redstone open` - opens Chrome window using Selenium, logs in to PloudOS, accesses server admin page and activates the server.
  * `!redstone close` - similar to the above command, deactivates the server
  * `!redstone stop` - similar to the above command, stops the server execution
  
## Usage

Coming soon!
