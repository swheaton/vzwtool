import time

import yaml
from selenium import webdriver

with open("config.yml", "r") as configFile:
    configs = yaml.safe_load(configFile)
    print(configs)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs',  {
        "download.default_directory": "./_data",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
        }
    )

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://login.verizonwireless.com/vzauth/UI/Login")

    elem = driver.find_element_by_id("IDToken1")
    elem.clear()
    elem.send_keys(configs['username'])

    elem = driver.find_element_by_id("IDToken2")
    elem.clear()
    elem.send_keys(configs['password'])

    driver.find_element_by_id("login-submit").click()
    print("Clicked login-submit");
    time.sleep(100)

    print("getting viewbill")
    driver.find_element_by_xpath("//*[@id='mvo_ovr_quick_updates_pos1']/div/div/div/div[3]/span/a/button").click()
    print("got view bill")

    time.sleep(100)

    driver.find_element_by_xpath("//*[@id='billStatusSection']/div/div/div[6]/div[2]/button").click()
    print("clicked bill pdf")

    time.sleep(1000)
    driver.close()
