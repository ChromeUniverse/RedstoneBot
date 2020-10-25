from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import discord
from discord.ext import commands


def get_status():
    # Change these placeholders with your actual PloudOS credentials
    username = "Username"
    password = "Password"

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://ploudos.com/login/")
    print(driver.title)


    # enter username and password
    username_input = driver.find_element_by_name("username")
    username_input.send_keys(username)

    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)

    source = ""

    try:
        # get rid of annoying privacy notice
        annoying_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sc-bwzfXH.jlyVur"))
        )
        annoying_button.click()

        print("Annoying button clicked!")

        # login
        login_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary"))
        )

        login_button.click()

        print("Login button clicked")

        # access ajax endpoint get JSON
        driver.get("https://ploudos.com/manage/s10434/ajax2")
        source = driver.page_source
    except:
        print("Something went wrong")

        
    driver.quit()


    # "converting" page source to JSON

    data = list(source)
    for i in range(25):
        data.pop(0)
    for i in range(14):
        data.pop()

    data = ''.join(data)

    data = json.loads(data)

    # printing useful data

    message = '\n'

    if data["status"] == 'READY':

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'
        message += '\nCPU: **' + str(data["serverUsedCPU"]) + '%** in use'
        message += '\nMemory: **' + str(data["serverUsedRAM"]) + ' MB** in use out of **' + str(data["serverMaxRam"]) + ' MB** max'
        message += '\nSSD storage: **' + str(data["serverUsedSpace"]/1000) + ' GB** used out of **' + str(data["serverTotalSpace"]/1000) + ' GB** max'
        message += '\n\n**Extra Info**\n'

        if data["isRunning"] == False:
            if data["isEditorMode"] == True:
                status = 'Server is running in Editor Mode'
            if data["isEditorMode"] == False:
                status = 'Server stopped'
        if data["isRunning"] == True:
            if data["isStarted"] == True:
                status = 'Server is up and running!'
                message += '\nPlayers online: **' + str(data["onlineCount"]) + '** out of **' + str(data["onlineMax"]) + '** max'
            if data["isStarted"] == False:
                status = 'Server is starting up!'

        message += '\nServer connection timeout is **' + str(data["serverTimeout"]) + '** seconds or **' + str(data["serverTimeoutFormatted"]) + '**'

    elif data["status"] == "SETUP":

        status = 'Server is running setup!'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    elif data["status"] == "CLOSING":

        status = 'Server is closing'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    elif data["status"] == "OFFLINE":

        status = 'Server is offline'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    elif data["status"] == "QUEUE":

        status = 'Server is in the queue!'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'
        message += '\n\n**Queue Info**\n'
        message += '\nQueue position: **' + str(data["queuePos"]) +'** out of **'+ str(data["queuePos"]) + '**'
        message += '\nApproximate waiting time: **' + str(data["queueTimeFormatted"]) + ' minute(s)**'

    elif data["status"] == "WAITING_FOR_ACCEPT":

        status = 'Waiting for user confirmation on admin page'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'
        message += '\n**Visit the admin page!**\n'

    return status, message

client = commands.Bot(command_prefix = '!redstone ')

token = 'NzY5NzYxMjcwMjY5NDc2ODg3.X5TuDA.dd0uzRNkNssAaZwBwbt4GiB015c'

# bot startup
@client.event
async def on_ready():
    print('Bot is ready.')

# pinng command - replies with "Pong!" + connection latency in miliseconds
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Connection latency is {round(client.latency * 1000)}ms')

@client.command()
async def status(ctx):
    await ctx.send('Hold on to your hats! Getting server status... this might take a while.')
    start = time.time()
    status, message = get_status()
    page1=discord.Embed(
        title=status,
        description=message,
        colour=discord.Colour.from_rgb(221,55,55)
    )
    await ctx.send(embed=page1)
    end = time.time()
    await ctx.send(f'\n\nServer status fetching took ~**{round(end - start + client.latency)} seconds**.')


client.run(token)
