# RedstoneBot

A Discord bot made for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/), originally built for the SMP BR community.

This bot was built with [Python 3](http://python.org/), [Requests](https://requests.readthedocs.io/en/master/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [discord.py](https://github.com/Rapptz/discord.py).

Built (mostly) for educational purposes.

## Gallery

![image](https://i.postimg.cc/vm24YCqR/redstone2-1.png)


## Commands

### DEPRECATED

`!redstone help`

Shows help page and commands.

`!redstone ping`

Replies with "Pong!" and shows connection latency in miliseconds.

`!redstone status`

Shows current server status: "Online", "In queue", "Starting up", etc.

Shows additional info about server resources, number of online players, and more.

`!redstone queueTime`

Shows server locations and queue waiting times.

`!redstone start [location]`

Puts your server in the activation queue. Specify the server location with `[1]` (Nuremberg) or `[2]` (St. Louis).

You only need to run this once: it automatically sends user confirmation when you reach the top spot of the queue.

`!redstone stop`

If the server is "Online", this will deactivate the server.

`!redstone restart`

If the server is "Stopped", this will reactivate the server.


## Folder Structure 

### DEPRECATED

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
|   ├── queuetime.py        # scrapes ploudos.com for queue waiting times
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


## Usage

**WARNING: DEPRECATED AS OF JAN. '21**

* Install and set up dependencies: (Ubuntu Linux shown below)
  * discord.py:

  ```
  python3 -m pip install -U discord.py
  ```

  * Selenium for Python:

  ```
  python3 -m pip install selenium
  ```

  * Chromium web browser:

  ```
  sudo apt install chromium-browser
  ```

  * Chrome webdriver (v87 shown below, check your version):

  ```
  wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
  ```
  * Unzip `chromedriver.zip`:

  ```
  sudo apt install unzip
  unzip chromedriver.zip
  ```

  * Copy PATH to `chromedriver` and paste in `bot.py`:

  ```
  PATH = "path/to/webdriver/goes/here/chromedriver"
  ```

* Edit your credentials in `bot.py`:
```
# Change these placeholders with your actual PloudOS credentials
username = "ChromeUniverse"
password = "12345678"

# The secret bot token!
token = 'abcdefgh_12345678'
```

* After you registered your bot in the [Discord Developers Portal](https://discord.com/developers/applications) and added it to your server, run `bot.py`.

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
  * Auto-confirm on `!redstone start`
  * Server location selector
  * Displays queue waiting times

* Credentials now stored in separate file

* Added new project folder structure - Special thanks to Kriasoft and their [Folder Structure Conventions](https://github.com/KriaSoft/Folder-Structure-Conventions)


## To-do List

* Add serverID customization/set-up
* Add instructions on how to add RedstoneBot to other servers
* In `bot.py`:
  * Refine some stuff here and there - mostly Async code and auto-confirm
  * Add separate files for each command/main Async function
  * Switch from Requests to aiohttp? (does this even make sense?)
* Scalability
* Improve code robustness
* Add a log file
* Commands to add:
  * `!redstone info` - displays important server info, such as name, version, IP, port, resources and more.
* Prepare a Release to deploy *RedstoneBot* to AWS Lightsail


## Disclaimer

This bot isn't publicly available. It was made to be used exclusively by the SMP BR Discord.

If you want to use this bot in your own Discord server, clone this repo, create a Discord bot (visit the [Discord Developers Portal](https://discord.com/developers/applications)) and host it or your local machine or VPS (AWS Lightsail, Linode, etc.)

## License

This open-source project is released under the GNU GPL v3.0 license. Check the `LICENSE` file for more details.
