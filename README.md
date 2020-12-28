# RedstoneBot

The goal of this branch is to migrate web scraping functionality from Selenium to [Requests](https://requests.readthedocs.io/en/master/), whenever possible. 

This should improve performance, robustness, and reduce _RedstoneBot_'s dependencies.


## Commands that now use Requests

No commands use Requests, yet!

## Progress

* Created `api_request.py` for testing the Requests module on PloudOS.com
  * Succesfuly logs in
  * Gets response from internal PloudOS API
  * Decodes response using JSON

## To-do List

* On `api_request.py`:
  * Add support for "Curerntly in maintenance mode, check back later"
* Integrate `api_request.py` into `bot.py`
* Migrate from Selenium to Requests:
  * `login()` function
  * `!redstone status` command
* Do some more network sniffing in PloudOS.com!
  * Find exactly what requests are performed to activate the server, enter the queue, authenticate, deactivate, etc.
