# RedstoneBot

<!--

## 🛑 DEPRECATION NOTICE 🛑

As of January 2021, Erik, creator and owner of PloudOS servers, has activated Cloudflare DDoS protection on the [PloudOS website](ploudos.com). 

It consists mostly of a JavaScript challenge that can only be solved by regular web browsers and prevents crawlers, bots and webscrapers like _RedstoneBot_ to make requests and access web services.

The _RedstoneBot_ team (myself and [Eduardo](https://github.com/qrno/)) is trying to find a way to bypass the JS challenge. Until then, _RedstoneBot_ is **deprecated**.

We're trying to find a suitable dependency to bypass the challenge. In the worst case, we'll be conducting a fair amount of network sniffing and research to develop our own challenge solver.

Thanks to [Steven](https://github.com/scaredos/) for his work on reverse engineering CloudFlare challenges. Check out his [cfresearch](https://github.com/scaredos/cfresearch) repo for more information.




## Overview

-->

A Discord bot made for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/), originally built for the SMP BR community.

This bot was built with [Python 3](http://python.org/), [Selenium for Python](https://selenium-python.readthedocs.io/#), [JSON](https://docs.python.org/3/library/json.html) (pre-installed with Python3), [Requests](https://requests.readthedocs.io/en/master/) and [discord.py](https://github.com/Rapptz/discord.py)

Built (mostly) for educational purposes.

## Gallery

![image](https://i.imgur.com/Gcsp2Oc.png)

## Commands

`!redstone ping` 

Replies with "Pong!" and shows connection latency in miliseconds.

`!redstone status` 

Shows current server status: "Online", "In queue", "Starting up", etc., along with additional info about server resources, number of online players, and more (see picure above for example).

`!redstone open` 

Activates the server (run twice: once when opening, once more when waiting for confirmation).

`!redstone close` 

Deactivates the server.

## To-do List

* Migrate from Selenium to [Requests](https://requests.readthedocs.io/en/master/) - Check the `requests` branch for more details! 
* Improve code robustness
* Add a log file
* Commands to add:
  * `!redstone info` - displays important server info, such as name, version, IP, port, resources and more.
  * `!redstone stop` - similar to the `open` and `close`; stops the server.
* Prepare a Release to deploy *RedstoneBot* to AWS Lightsail
  
## Usage

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

## Disclaimer

This bot isn't publicly available. It was made to be used exclusively by the SMP BR Discord. 

If you want to use this bot in your own Discord server, clone this repo, create a Discord bot (visit the [Discord Developers Portal](https://discord.com/developers/applications)) and host it or your local machine or VPS (AWS Lightsail, Linode, etc.)

## License

This open-source project is released under the GNU GPL v3.0 license. Check the `LICENSE` file for more details.


