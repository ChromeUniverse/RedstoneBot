# RedstoneBot

The goal of this branch is to migrate web scraping functionality from Selenium to [Requests](https://requests.readthedocs.io/en/master/), whenever possible.

This should improve performance, robustness, and reduce _RedstoneBot_'s dependencies.

## Folder Structure

```
.
├── code                    # source code
|   ├── bot.py              # Discord commands, Requests session
|   ├── credentials.py      # PloudOS credentials, Discord token
|   ├── urls.py             # list of URLs
|   ├── login.py            # logs in to ploudos.com
|   ├── functions.py        # main async function definitions
|   └── format.py           # formats Rich Embeds
|
├── experiments             # Python files for experiments
|   ├── api_request.py      # testing requests and API calls
|   ├── autostart.py        # automatically enters queue and starts server
|   ├── credentials.py      # see 'code' folder above
|   └── format.py           # see 'code' folder above
|
├── api.json                # collection of API calls and JSON responses
├── requests.txt            # PloudOS network sniffing analysis report
├── requirements.txt        # pip packages
|
├── LICENSE                 # GNU GPL v3.0 License
└── README.md               # you're reading this right now!
```


## Commands that now use Requests

* `!redstone ping`
* `!redstone status`
* `!redstone start`
* `!redstone accept`
* `!redstone stop`
* `!redstone restart`

## Progress

* Created `api_request.py` to test the Requests module on PloudOS.com
  * Succesfully logs in
  * Gets response from internal PloudOS API
  * Decodes response using JSON
  * Can deal with "Currently in maintenance mode, check back later" errors/messages

* Updated `bot.py`.
  * Now handles all actions with calls to internal PloudOS API
  * Async functions/API calls _(needs refinement)_
  * Added foolproofness - commands are only executed if server is in the appropriate state (i.e. the bot won't try to open the server once it's already online)
  * Auto-confirm on `!redstone start` _(needs refinement)_

* Credentials now stored in separate file

* Added new project folder structure - Special thanks to Kriasoft and their [Folder Structure Conventions](https://github.com/KriaSoft/Folder-Structure-Conventions)


## To-do List

* In `bot.py`:
  * Refine some stuff here and there - mostly Async code and auto-confirm
  * Add separate files for each command/main Async function
* Scalability
