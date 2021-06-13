# RedstoneBot

A Discord bot for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/), originally built for the SMP BR Discord community.

This bot was built with [Python 3.8](http://python.org/), [AIOHTTP](https://docs.aiohttp.org/en/stable/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [discord.py](https://github.com/Rapptz/discord.py).

_**Want to add this bot to your Discord server?**_ [Now you can!](https://chromeuniverse.github.io/RedstoneBot/manual) Redstone is now hosted on AWS Lightsail and runs non-stop, 24/7.

_**Want to create you own clone of this bot?**_ Head over to the `USAGE` section below.

More non-technical info available at [RedstoneBot's official website](https://chromeuniverse.github.io/RedstoneBot/).

Note: This bot was built for educational purposes.

## Gallery

![image](https://i.postimg.cc/vm24YCqR/redstone2-1.png)


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


## Usage (Ubuntu Linux)

Follow these steps to create a clone of RedstoneBot.

**0. Register your bot app in the [Discord Developers Portal](https://discord.com/developers/applications)** 

**1. Make sure you have Python 3 and Pip installed on your machine**

`python3 --version`

`pip3 --version`

If you don't, install them:

`sudo apt update`

`sudo apt install python3`

`sudo apt install pip3`

**2. Clone this repo**

`git clone https://github.com/ChromeUniverse/RedstoneBot.git`

**3. Install and set up dependencies with Pip**
  
`pip3 install -r requirements.txt`

**5. Change directory**

`cd RedstoneBot/code/`

**6. Edit your credentials in `credentials.py`**

`nano credentials.py`

```
# Change these placeholders with your actual PloudOS credentials
username = "ChromeUniverse"
password = "12345678"

# The secret bot token!
token = 'abcdefgh_12345678'
```

**7. Run the Bash script with `nohup`**

`nohup bash script.sh`


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
  * Add Discord to PloudOS server linking (only one PloudOS server per guild, currently)
  * Async requests with AIOHTTP
  * Separate files for most important functions

* Credentials now stored in separate file

* Added new project folder structure - Special thanks to Kriasoft and their [Folder Structure Conventions](https://github.com/KriaSoft/Folder-Structure-Conventions)


## To-do List

* Add some CI/CD
  * Bot testing
  * GitHub Actions?
  * Automatically deploy code to Lightsail VPS 
* In `bot.py`:
  * Refine some stuff here and there - mostly Async code and auto-confirm
    * Async JSON parsing?
    * Async CSV/Database reading/writing?
  * Add multiple activation loops - one per Discord guild
* Switch databases from CSV to SQLite3 (would this make sense?)
* Add a log file
* Commands to add:
  * `!redstone info` - displays important server info, such as name, version, IP, port, resources and more.


## License

This open-source project is released under the GNU GPL v3.0 license. Check the `LICENSE` file for more details.
