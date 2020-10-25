from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

username = "ChromeUniverse"
password = "Ln!TN2ud2M-CQSS"

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

# close Chrome window
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

print('\n* SERVER INFO *')
print('\nServer name: ' + str(data["serverName"]))
print('\nCurrently running ' + str(data["serverVersion"]))
print('\nCPU: ' + str(data["serverUsedCPU"]) + '% in use')
print('Memory: ' + str(data["serverUsedRAM"]) + ' MB in use out of ' + str(data["serverMaxRam"]) + ' MB max')
print('SSD storage: ' + str(data["serverUsedSpace"]/1000) + ' GB used out of ' + str(data["serverTotalSpace"]/1000) + ' GB max')
print('\n* EXTRA INFO *\n')
print('Players online: ' + str(data["onlineCount"]) + ' out of ' + str(data["onlineMax"]) + ' max')
print('Is the server running? ' + str(data["isRunning"]))
print('Has the server started yet? '+ str(data["isRunning"]))
print('\nServer connection timeout is ' + str(data["serverTimeout"]) + ' seconds or ' + str(data["serverTimeoutFormatted"]))
