import time

import yaml
import traceback
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Login to VZW with username and password on selenium
def login(driver, username, password):
    driver.get("https://login.verizonwireless.com/vzauth/UI/Login")

    elem = driver.find_element_by_id("IDToken1")
    elem.clear()
    elem.send_keys(username)

    elem = driver.find_element_by_id("IDToken2")
    elem.clear()
    elem.send_keys(password)

    driver.find_element_by_id("login-submit").click()
    print("Clicked login-submit")

# Wait for button to be clickable then click it
def waitAndClick(driver, xpath):
    print("waiting for elt to be clickable")
    element = WebDriverWait(driver, 100).until(
        expected_conditions.element_to_be_clickable((By.XPATH, xpath))
    )
    print("elt available to click, about to do so")
    element.click()
    print("elt clicked")

with open("config.yml", "r") as configFile:
    configs = yaml.safe_load(configFile)
    print(configs)
    # "download.default_directory": "_data/",

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs',  {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
        }
    )

    driver = webdriver.Chrome(options=chrome_options)

    login(driver, configs['username'], configs['password'])

    try:
        waitAndClick(driver, "//*[@id='mvo_ovr_quick_updates_pos1']/div/div/div/div[3]/span/a/button")
        waitAndClick(driver, "//*[@id='billStatusSection']/div/div/div[6]/div[2]/button")
    except TimeoutError:
        print("Timed out trying to get bill")
    except Exception as e:
        print(traceback.format_exc())

    # Wait for file to be downloaded then quit
    time.sleep(5)
    driver.quit()
