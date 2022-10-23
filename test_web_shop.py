import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://demowebshop.tricentis.com/')


def test_notebooks_page():
    driver.find_element(By.XPATH, "//li[@class='inactive']//a[normalize-space()='Computers']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@title='Show products in category Notebooks'][normalize-space()='Notebooks']").click()
    time.sleep(2)

    assert driver.current_url == 'https://demowebshop.tricentis.com/notebooks', 'Error, another page'


def test_register():
    driver.find_element(By.CSS_SELECTOR, '.ico-register').click()
    driver.find_element(By.ID, 'FirstName').send_keys('Anna')
    driver.find_element(By.ID, 'LastName').send_keys('Smith')
    driver.find_element(By.ID, 'Email').send_keys('sirius4@mail.com')
    driver.find_element(By.ID, 'Password').send_keys('123456')
    driver.find_element(By.ID, 'ConfirmPassword').send_keys('123456')
    driver.find_element(By.ID, 'register-button').click()

    assert driver.current_url == 'https://demowebshop.tricentis.com/registerresult/1', 'Error, another page'
    time.sleep(2)

 #   driver.quit()

