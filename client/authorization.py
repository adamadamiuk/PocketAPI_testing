from selenium import webdriver
import requests

from client.security.user_config import UserBase
from locators import *
from resources import *

"""
Pocket API require some initial setting to allow requests.
It has already been done for this test purpose.
"""

headers = {"X-Accept": "application/json"}
driver = webdriver.Chrome(executable_path='D:/software/chromedriver.exe')


def auth_code():
    payload = {
        "consumer_key": KEY,
        "redirect_uri": REDIRECT_URL}

    response = requests.post(f"{BASE_URL}/v3/oauth/request", data=payload, headers=headers)
    req_code = response.json()["code"]
    return req_code
    # obtaining request code


def authorization_token(req_code):
    url = f"{BASE_URL}/auth/authorize?request_token={req_code}&redirect_uri={REDIRECT_URL}"
    driver.get(url)
    login_name = UserBase.decode_user()["username"]
    login_pass = UserBase.decode_user()["password"]
    name_field = driver.find_element_by_css_selector(USERNAME_LOCATOR)
    pass_field = driver.find_element_by_css_selector(PASS_LOCATOR)
    button = driver.find_element_by_css_selector(AUTH_BUTTON_LOCATOR)
    name_field.click()
    name_field.send_keys(login_name)
    pass_field.click()
    pass_field.send_keys(login_pass)
    button.click()
    driver.close()
    # logging in using Selenium

def access_token(req_code):
    authorization_token(req_code)
    payload = {
        "consumer_key": KEY,
        "code": req_code}

    response = requests.post(f"{BASE_URL}/v3/oauth/authorize", data=payload, headers=headers)
    acc_token = response.json()["access_token"]
    return acc_token
    # obtaining access token


