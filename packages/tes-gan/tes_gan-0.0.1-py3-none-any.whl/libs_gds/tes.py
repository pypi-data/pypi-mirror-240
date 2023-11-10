from itertools import count
import time
from subprocess import check_call
import os
from threading import Thread
from base64 import b64decode, b64encode

## *********************************************************** SELENIUM
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
## *********************************************************** SELENIUM

user = "admin"
type_akun = "0"
dirImg = "C:/WORKER/BOT/GDS BOT/video/"

chrome= [
        (1, dirImg)
      ]

tot_chrome  = len(chrome)
threads = []

def show(b):
    return b64decode(b).decode()

def myFunction(delay, dirImg):
    time.sleep(delay)
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    driver.get("https://whoer.net/")
    time.sleep(2)

    el_ip = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='main']/section[1]/div/div/div/div[1]/div/strong"))
    )
    res_ip = el_ip.text
    print(f'my_ip = "{res_ip}"')

i = 0
while i < 1:
    for devices in chrome:
        t = Thread(target=myFunction, args=(devices))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

        if len(threads) == tot_chrome:
            print("                            ")
            print("Muterr Maneh Boskuuu..")
            print(len(threads))
            print("                            ")
            threads = []