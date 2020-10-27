# RedstoneBot

A Discord bot built for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/), originally built for the SMP BR community.

This bot was built with [Python 3](http://python.org/), [Selenium for Python](https://selenium-python.readthedocs.io/#), [JSON](https://docs.python.org/3/library/json.html) and [Discord.py](https://github.com/Rapptz/discord.py)

![image](https://i.imgur.com/Gcsp2Oc.png)


## Commands

* `!redstone ping` Replies with "Pong!" and show connection latency in miliseconds
* `!redstone status` Shows current server status: "Online", "In queue", "Starting up", etc., along with additional info about server resources, number of online players, and more (see picure above for example)
* `!redstone open` - Activates the server (run twice: once when opening, once more when waiting for confirmation)
* `!redstone close` - Deactivates the server

## To-do List

* Migrate from Selenium to [Requests](https://requests.readthedocs.io/en/master/)
* Commands to add:
  * `!redstone stop` - similar to the above command, stops the server execution
  
## Usage

Coming soon!
