# RedstoneBot

A Discord bot for interacting with Minecraft servers hosted by [PloudOS](https://ploudos.com/).

This bot was built with [Python 3](http://python.org/), [AIOHTTP](https://docs.aiohttp.org/en/stable/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [discord.py](https://github.com/Rapptz/discord.py), and [distest](https://distest.readthedocs.io/).


### _Want to add this bot to your Discord server?_

[Now you can!](http://34.200.98.64/redstone-quickstart) Redstone is now hosted on AWS Lightsail and runs non-stop, 24/7.

### _Join the [RedstoneBot Discord](https://discord.gg/HDkaQu8Rdt) now!_

Get the latest news on the development of RedstoneBot, chat with the developers, report issues/bugs, suggest new features, and more!

### _Want to create you own clone of this bot?_

Then head over to the [Usage](#usage) section below.

More non-technical info available at [RedstoneBot's official webpage](http://34.200.98.64/redstone).

**Note**: This project was made exclusively for educational purposes.

## Gallery

![image](https://i.postimg.cc/vm24YCqR/redstone2-1.png)


## Folder Structure 

```
.
├── .github/workflows                  
|   └── ci-cd.yaml          # build/test/deploy workflow
|
├── code                    # source code
├── experiments             # Python files for experiments
|
├── api.json                # collection of API calls and JSON responses
├── requests.txt            # PloudOS network sniffing analysis report
├── requirements.txt        # list of pip packages
|
├── LICENSE                 # GNU GPL v3.0 License
└── README.md               # you're reading this right now!
```


## Usage

Follow these steps to create and host a clone of RedstoneBot.

Please note: the following procesures are optimized for Ubuntu Linux and similar distros.

**0. Register your bot app in the [Discord Developers Portal](https://discord.com/developers/applications) and create a new account for your bot in the [PloudOS registration page](https://ploudos.com/register/).** 

**1. Install Python 3 and Pip**

`sudo apt update`

`sudo apt install python3`

`sudo apt install pip3`

**2. Clone this repo**

`git clone https://github.com/ChromeUniverse/RedstoneBot.git`

**3. Install dependencies with Pip**
  
`pip3 install -r requirements.txt`

**4. `cd` into the source code folder**

`cd RedstoneBot/code/`

**5. Set environment variables**

Open the `/etc/environment` file with your preferred editor and set the following global environment variables.

`vim /etc/environment`

```
# required

PLOUDOS_USERNAME='MyRedstoneBotClone'
PLOUDOS_PASSWORD='123456'
BOT_TOKEN='secret_discord_bot_token_goes_here'
BOT_PREFIX='!test'

# optional - CI/CD, testing, etc.

PLOUDOS_IP='verycoolserver.ploudos.me'
CI_TOKEN='secret_discord_bot_token_goes_here'
TESTER_TOKEN='secret_discord_bot_token_goes_here'
REDSTONE_TOKEN='secret_discord_bot_token_goes_here'
```

### Brief explanation

* Required environment variables:

  * `PLOUDOS_USERNAME` and `PLOUDOS_PASSWORD` are the credentials for the bot account you created in step 0.

  * `BOT_TOKEN` is the Discord bot token and `BOT_PREFIX` is your choice of bot prefix.

* Optional anevironment variables - useful for local development: making CI/CD workflows, writing tests with [distest](https://distest.readthedocs.io/), etc.

  * `PLOUDOS_IP` is the address of your server.
  * `CI_TOKEN` is the token of a Discord bot app for running a CI version of your code.
  * `TESTER_TOKEN` is the token of a Discord bot for running tests against your CI bot.
  * `REDSTONE_TOKEN` is the token of a Discord bot app for deploying your code.

Remember to log out and log back in for these changes to take effect.

**6. Run your bot**

A simple way to run your bot in your machine's background is to use `nohup`:

`nohup bot.py &`

But a more reliable way to do this is with the [PM2](https://pm2.keymetrics.io/) process manager for Node.js:

`sudo apt install nodejs`

`sudo apt install npm`

`sudo npm install -g pm2`

Run [bot.py with PM2](https://stackoverflow.com/questions/49109069/running-a-python-script-with-pm2-error):

`pm2 start bot.py --interpreter python3`

```
[PM2] Applying action restartProcessId on app [bot](ids: [ 1 ])
[PM2] [bot](1) ✓
[PM2] Process successfully started
┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
│ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
│ 0  │ bot                │ fork     │ 10   │ online    │ 0%       │ 34.0mb   │
└────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
```

## License

This open-source project is released under the GNU GPL v3.0 license. Check the `LICENSE` file for more details.

© Lucca Rodrigues 2021. All rights reserved. 
