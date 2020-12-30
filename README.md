# RedstoneBot

The goal of this branch is to migrate web scraping functionality from Selenium to [Requests](https://requests.readthedocs.io/en/master/), whenever possible. 

This should improve performance, robustness, and reduce _RedstoneBot_'s dependencies.


## Commands that now use Requests

* `!redstone ping` 
* `!redstone status` (lacking proper formatting)
* `!redstone open`
* `!redstone accept`
* `!redstone stop`
* `!redstone start`

## Progress

* Created `api_request.py` to test the Requests module on PloudOS.com
  * Succesfuly logs in
  * Gets response from internal PloudOS API
  * Decodes response using JSON
  * Can deal with "Currently in maintenance mode, check back later" errors/messages
  
* Updated `bot.py`.
  * Now handles all actions with calls to internal PloudOS API
  * Async functions/API calls


## To-do List

* In `bot.py`:
  * `!redstone open`: repeatedly call API, get status, and automatically run `!redstone accept` when necessary
* Add separate `credentials.txt` file - stores Username, Password, serverID, Discord bot token
* Do some more network sniffing!
  * Find exactly which requests are performed to activate the server, enter the queue, authenticate, deactivate, etc.
