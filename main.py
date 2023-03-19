import datetime

import undetected_chromedriver as uc

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import random
import time
import asyncio

from selenium.common.exceptions import TimeoutException,ElementClickInterceptedException,ElementNotInteractableException,StaleElementReferenceException,NoSuchElementException
from termcolor import colored
from database import ConnectDb,Art

import colorama

colorama.init()


class Bot:
    def __init__(self):
        Art()

        opts = uc.ChromeOptions()

        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        opts.add_experimental_option("prefs", prefs)

        self.driver = uc.Chrome(options=opts, version_main=111, use_subprocess=True)

    def login_(self,login_email,login_password):
        self.link_url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

        self.driver.get(self.link_url)
        self.driver.set_window_size(980, 900)

        email_input = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="username"]')))

        email_input.send_keys(login_email)

        time.sleep(random.randrange(1,4))

        password_input = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="password"]')))

        password_input.send_keys(login_password)

        print(colored(f"[ ] {time.ctime()} Entered password and email","green"))
        time.sleep(random.randrange(1, 4))

        submit_form = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Sign in"]')))

        submit_form.click()

        print(colored(f"{time.ctime()} Logging in ..","green"))

        time.sleep(random.randrange(20, 40))


if __name__=="__main__":

    db=ConnectDb()
    credentials=db.check_credentials()

    email=credentials[0]
    password=credentials[1]

    Bot().login_(email,password)




