import time
import pytest
from setuptools import _distutils
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')

def test_title():
    title_site = driver.title
    assert title_site == 'Swag Labs'

def test_login_form():
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')
    time.sleep(1)
    user_password = driver.find_element(By.ID, 'password')
    user_password.send_keys('secret_sauce')
    time.sleep(1)
    button_login = driver.find_element(By.ID, 'login-button')
    button_login.click()
    time.sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Error, another site'

    driver.quit()

