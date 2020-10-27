# Broken

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

'''
# enabling options for headless Selenium operation
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
'''

# path to chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Good luck using these credentials :-)

# PloudOS login
username = "ChromeUniverse"
password = "7Sw3FcfNwBVNUxV"
# Discord bot token
token = 'NzY5NzYxMjcwMjY5NDc2ODg3.X5TuDA.-9rKSnMNq1e7em0HMqT74xx65Co'

# URLs
login_url = 'https://ploudos.com/login/'
api_url = 'https://ploudos.com/manage/s10434/ajax2'




#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
driver = webdriver.Chrome(PATH)

source = ""

# Login

driver.get(login_url)
print(driver.title)

# enter username and password
username_input = driver.find_element_by_name("username")
username_input.send_keys(username)

password_input = driver.find_element_by_name("password")
password_input.send_keys(password)

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

# gets server status
def get_status():

    # access ajax endpoint to get JSON
    driver.execute_script("window.open('https://ploudos.com/manage/s10434/ajax2','new window')")

    source = ''

    # switching to API endpoint url
    allTabs = driver.window_handles
    for tab in allTabs:
        driver.switch_to.window(tab)
        print('Switch!')
        if driver.current_url == 'https://ploudos.com/manage/s10434/ajax2':
            print('Found our page!')
            # get page source
            source = driver.page_source
            # close current tab
            driver.close()

    # "converting" page source to JSON
    data = list(source)
    for i in range(25):
        data.pop(0)
    for i in range(14):
        data.pop()

    data = ''.join(data)
    data = json.loads(data)

    print('The data be like: ' + str(data))
    # printing useful data

    message = '\n'

    if data["status"] == 'READY':

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

        message += '\n\n**Server resources**\n'
        message += '\nCPU: **' + str(data["serverUsedCPU"]) + '%** in use'
        message += '\nRAM: **' + str(data["serverUsedRAM"]) + ' MB** in use out of **' + str(data["serverMaxRam"]) + ' MB** max'
        message += '\nSSD: **' + str(data["serverUsedSpace"]/1000) + ' GB** used out of **' + str(data["serverTotalSpace"]/1000) + ' GB** max'

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

        status_message = 'Server is running setup!'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    elif data["status"] == "CLOSING":

        status_message = 'Server is closing'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    elif data["status"] == "OFFLINE":

        status_message = 'Server is offline'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'

    elif data["status"] == "QUEUE":

        status_message = 'Server is in the queue!'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'
        message += '\n\n**Queue Info**\n'
        message += '\nQueue position: **' + str(data["queuePos"]) +'** out of **'+ str(data["queuePos"]) + '**'
        message += '\nApproximate waiting time: **' + str(data["queueTimeFormatted"]) + ' minute(s)**'

    elif data["status"] == "WAITING_FOR_ACCEPT":

        status_message = 'Waiting for user confirmation on admin page'

        message += 'Server name: **' + str(data["serverName"]) + '**'
        message += '\nCurrently running **' + str(data["serverVersion"]) + '**'
        message += '\n**Visit the admin page!**\n'

    return status_message, message

def open_server():

    driver = webdriver.Chrome(PATH)
    login(driver)
    driver.get("https://ploudos.com/manage/s10434/")

    # clicking "Ligar" button
    button = driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
    print(button.text)
    button.click()


    try:
        # selecting German server (hosted in Nuremberg)
        DE_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div[2]/div/div[1]/div/a'))
        )
        DE_button.click()
    except:
        driver.quit()


# command prefix
client = commands.Bot(command_prefix = '!redstone ')

# bot startup
@client.event
async def on_ready():
    print('Bot is ready.')

# ping command - replies with "Pong!" + connection latency in miliseconds
@client.command()
async def ping(ctx):
    #await ctx.send(f'Pong! Connection latency is {round(client.latency * 1000)}ms')
    await ctx.send(f'Pong!')

# status command - server status and useful information
@client.command()
async def status(ctx):
    await ctx.send('Hold on to your hats! Getting server status... this might take a while.')
    start = time.time()
    status_message, message = get_status()
    embed_message=discord.Embed(
        title=status_message,
        description=message,
        colour=discord.Colour.from_rgb(221,55,55)
    )
    await ctx.send(embed=embed_message)
    end = time.time()
    await ctx.send(f'\n\nServer status fetching took ~**{round(end - start + client.latency)} seconds**.')


# open command - activates server
@client.command()
async def open(ctx):
    await ctx.send('Opening server... this is going to take a while.')
    open_server()

client.run(token)
