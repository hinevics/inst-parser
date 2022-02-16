from selenium import webdriver
from config import PATH_GECKODRIVER, USER_NAME, PASSWORD
import time

# Code 2
browser = webdriver.Firefox(executable_path=PATH_GECKODRIVER)
browser.get('https://www.instagram.com')
time.sleep(2)
username_el = browser.find_element_by_name('username')
password_el = browser.find_element_by_name('password')

time.sleep(2)
username_el.send_keys(USER_NAME)
time.sleep(2)
password_el.send_keys(PASSWORD)
submit_el = browser.find_element_by_css_selector("button[type='submit']")
time.sleep(1)
submit_el.click()
