# RedstoneBot

[![](https://github.com/ChromeUniverse/RedstoneBot/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/ChromeUniverse/RedstoneBot/actions/workflows/ci-cd.yaml)
[![](https://discord.com/api/guilds/853346901545844736/embed.png?style=shield)](https://discord.gg/HDkaQu8Rdt)


## DEPRECATION NOTICE

### RedstoneBot will be shut down, permanently, no later than August 14, 2021.

All RedstoneBot-related development activities have been ceased and this repo will soon be archived.

Documentation for RedstoneBot (including technical docs, guides, etc.) will still be available for the foresseable future.

**For more information, please read[ this post](http://34.200.98.64/redstone-shutdown).**

Thank you for using RedstoneBot!

---

A Discord bot for interacting with Minecraft servers hosted at [PloudOS](https://ploudos.com/).

This bot was built with [Python 3](http://python.org/), [AIOHTTP](https://docs.aiohttp.org/en/stable/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [discord.py](https://github.com/Rapptz/discord.py), and [distest](https://distest.readthedocs.io/).


### _Want to add this bot to your Discord server?_

[Now you can!](http://34.200.98.64/redstone-quickstart) Redstone is now hosted on AWS Lightsail and runs non-stop, 24/7.

### _Join the [RedstoneBot Discord](https://discord.gg/HDkaQu8Rdt) now!_

Get the latest news on the development of RedstoneBot, chat with the developers, report issues/bugs, suggest new features, and more!

### _Want to create your own clone of this bot?_

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

**5. Create a CSV database**

`vim db.csv`

This database need at least one row of dummy data so that the bot can work properly.

Enter the following line and save the file.

```mumbojumbo
1, 1, 1, 1
```


**6. Set environment variables**

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

**7. Run your bot**

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

**8. Test your bot**

* Create a new bot application on the [Discord Developers Portal](https://discord.com/developers/applications) that will serve as your **tester bot**.

* Before configuring the tester bot, setup the (not so) optional (right now) environment variables described in **step 5**.

* Edit `tester_setup.py`.

  `vim tester_setup.py`

  ```py3
  # Replace this with the RedstoneBot clone's ID
  target_id = '862776943522611201'               

  # Replace this with the testing channel's ID
  channel_id = '853346992986128414'

  prefix = '!ci'       
  ```

  Notes: 

  * `target_id` - this is the ID of your main bot.

  * `channel_id` - this is the ID of the channel in which you will run your tester bot and your main bot.

  * `prefix` - this is the command prefix that the tester bot will use to send test commands.

* Run the tester bot:

  `python3 tester.py`

**9. Automate build, testing and deployment**

_Please note_: the following steps are optimized for automating workflows on GitHub Actions.

The repo you cloned already comes with a `.github/workflows` directory and a functional workflow for building, running tests, and deploying the bot to a remote host.

I deploy RedstoneBot through GitHub Actions to an AWS Lightsail virtual machine running Ubuntu Linux, but since this might not your case, chances are you'll need to modify the workflow file and add repo secrets.

**Prerequisites:**

* Make sure you have SSH access configured on the VPS that you'll deploy your bot to.

* Create a new bot application at the [Discord Developers Portal](https://discord.com/developers/applications) that will run your CI code.

* Create a new repo on GitHub for your clone bot.

* Add the following repo secrets:

  * `CI_TOKEN` - Discord bot token for your continuous integration bot.

  * `DEPLOYKEY` - Your SSH private key encoded as Base64

  * `PLOUDOS_IP` - The IP address of your PloudOS server

  * `PLOUDOS_USERNAME` - Your bot account's PloudOS username.

  * `PLOUDOS_PASSWORD` - Your bot account's PloudOS password.

  * `TESTER_TOKEN` - Discord bot token for your tester bot.

**Steps:**

* Modify the last two commands from the workflow file to your needs:

  ```yaml
  # Rsync over SSH - tranfer files with deployment.key
  - name: Sync files with AWS Lightsail             
    run:           
      rsync -zaPv -e "ssh -v -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i deployment.key" ./ ubuntu@34.200.98.64:~/RedstoneBot/    

  # SSH command
  - name: Restart bot      
    run:                     
      ssh -v -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i deployment.key ubuntu@34.200.98.64 bash /home/ubuntu/RedstoneBot/update.sh
  ```

* Now push your code to your new GitHub repo.

* Follow **Steps 1 through 7** on your VPS, if you haven't already.

* Finally, re-run any Actions jobs if you need to.

## License

This open-source project is released under the GNU GPL v3.0 license. Check the `LICENSE` file for more details.

© Lucca Rodrigues 2021. All rights reserved. 
