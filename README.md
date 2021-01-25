# RedstoneBot

A Discord bot made for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/), originally built for the SMP BR community.

This bot was built with [Python 3.8](http://python.org/), [AIOHTTP](https://docs.aiohttp.org/en/stable/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [discord.py](https://github.com/Rapptz/discord.py).

Built (mostly) for educational purposes.

## Gallery

![image](https://i.postimg.cc/vm24YCqR/redstone2-1.png)

## Disclaimer

This bot isn't available for public use, at least not yet. It was made to be used exclusively by the SMP BR Discord.

RedstoneBot is under contant development and refinement. Once it's ready for public use, this section will be updated and a public link to add this bot to your own server will be at the very top of this README.

For now, if you want to use this bot in your own Discord server, you can follow the `USAGE` section below.

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


## License

This open-source project is released under the GNU GPL v3.0 license. Check the `LICENSE` file for more details.
