from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import discord
from discord.ext import commands

chrome_options = Options()
chrome_options.headless = True
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

PATH = "C:\Program Files (x86)\chromedriver.exe"

# Change these placeholders with your actual PloudOS credentials
username = "username"
password = "password"

# The secret bot token!
token = 'bot_token_goes_here'

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
#driver = webdriver.Chrome(PATH)

def login(driver):

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

    except:
        print("Something went wrong")
        driver.quit()


def get_status(close_driver):

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
    #driver = webdriver.Chrome(PATH)
    login(driver)
    # access ajax endpoint get JSON
    driver.get("https://ploudos.com/manage/s10434/ajax2")
    source = driver.page_source

    if close_driver == True:
        driver.quit()
        print('Status acquired and driver closes')
    else:
        print('Status acquired and driver still open')
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
        message += '\n\n**Server Resources**\n'
        message += '\nCPU: **' + str(data["serverUsedCPU"]) + '%** in use'
        message += '\nMemory: **' + str(data["serverUsedRAM"]) + ' MB** in use out of **' + str(data["serverMaxRam"]) + ' MB** max'
        message += '\nSSD storage: **' + str(data["serverUsedSpace"]/1000) + ' GB** used out of **' + str(data["serverTotalSpace"]/1000) + ' GB** max'
        message += '\n\n**Extra Info**\n'

        if data["isRunning"] == False:
            if data["isEditorMode"] == True:
                status = 'Server is running in Editor Mode.'
            if data["isEditorMode"] == False:
                status = 'Server stopped.'
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

        status = 'Server is offline.'

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

        status = 'Waiting for user confirmation on admin page.'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'
        message += '\n**Visit the admin page!**\n'

    if close_driver == False:
        return status, message, driver
    return status, message

def open_server():
    print("Fetching server status......")
    status, message, driver = get_status(False)
    if status == 'Server is running in Editor Mode.':
        print('editorMode')
        driver.quit()
        return status
    if status == 'Server stopped.':
        print('stopped')
        driver.quit()
        return status
    if status == 'Server is up and running!':
        print('online')
        driver.quit()
        return status
    if status == 'Server is starting up!':
        print('start_up')
        driver.quit()
        return status
    if status == 'Server is running setup!':
        print('setup')
        driver.quit()
        return status
    if status == 'Server is closing.':
        print('closing')
        driver.quit()
        return status
    if status == 'Server is offline.':
        print('offline')
        print("Proceeding to open server!")
        #driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
        #driver = webdriver.Chrome(PATH)
        #login(driver)
        print('Login complete!')
        driver.get("https://ploudos.com/manage/s10434/")
        print('Got server admin page!')
        try:
            activate_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="buttons"]/a[1]'))
            )
            activate_button.click()
            #driver.implicitly_wait(1)
            print('Activate button clicked!')

            DE_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[1]/div/a'))
            )
            print('DE_button located')
            DE_button.click()
            print('DE_button clicked!')

            return 'Server activation in progress! Check the server status with `!redstone status`.'

        except:
            print('Something went wrong with server opening')
            return 'Something went wrong with server opening! Try again, maybe?'
        driver.quit()

    if status == 'Server is in the queue!':
        print('queue')
        driver.quit()
        return status
    if status == 'Waiting for user confirmation on admin page.':
        print('waiting for accept')
        #driver = webdriver.Chrome(PATH)
        driver.get("https://ploudos.com/manage/s10434/")
        try:
            accept_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="buttons"]/a'))
            )
            accept_button.click()
            #driver.implicitly_wait(1)
            print('Accept button clicked!')
        except:
            print('Something went worng with accept')
            return 'Something went wrong with confirmation! Try again, maybe?'
        driver.quit()
        return 'Server activation confirmed! Start up will commence shortly. Check the server status with `!redstone status`.'

def close_server():
    print("Fetching server status......")
    status, message = get_status(True)
    if status == 'Server is running in Editor Mode.':
        print('editorMode')
        return status
    if status == 'Server stopped.':
        print('stopped')
        return status
    if status == 'Server is up and running!':
        print('online')
        print("Proceeding to close server!")

        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
        #driver = webdriver.Chrome(PATH)
        login(driver)
        driver.get("https://ploudos.com/manage/s10434/")

        try:
            activate_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="buttons"]/a[2]'))
            )
            activate_button.click()

            return 'Server deactivation in progress! Check the server status with `!redstone status`.'

        except:
            driver.quit()
            print('Something went wrong with server closing')

    if status == 'Server is starting up!':
        print('start_up')
        return status
    if status == 'Server is running setup!':
        print('setup')
        return status
    if status == 'Server is closing.':
        print('closing')
        return status
    if status == 'Server is offline.':
        print('offline')
        return status
    if status == 'Server is in the queue!':
        print('queue')
        return status
    if status == 'Waiting for user confirmation on admin page.':
        print('waiting for accept')
        return status



client = commands.Bot(command_prefix = '!redstone ')

# bot startup
@client.event
async def on_ready():
    print('Bot is ready.')

# pinng command - replies with "Pong!" + connection latency in miliseconds
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! :ping_pong: Connection latency is {round(client.latency * 1000)}ms')

@client.command()
async def status(ctx):
    await ctx.send('Hold on to your hats! Fetching server status... this might take a while.')
    start = time.time()
    status, message = get_status(True)
    page1=discord.Embed(
        title=status,
        description=message,
        colour=discord.Colour.from_rgb(221,55,55)
    )
    await ctx.send(embed=page1)
    end = time.time()
    await ctx.send(f'\n\nServer status fetching took ~**{round(end - start + client.latency)} seconds**.')

opening = False

@client.command()
async def open(ctx):
    await ctx.send('Opening server... please wait.')
    message = open_server()
    await ctx.send(message)

@client.command()
async def close(ctx):
    await ctx.send('Closing server... please wait.')
    message = close_server()
    await ctx.send(message)

client.run(token)
