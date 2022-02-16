from selenium import webdriver
from config import PATH_GECKODRIVER, USER_NAME, PASSWORD, URL_USER
import time

# Request for access
browser = webdriver.Firefox(executable_path=PATH_GECKODRIVER)
browser.get(URL_USER)
time.sleep(2)
username_el = browser.find_element_by_name('username')
password_el = browser.find_element_by_name('password')

# login
time.sleep(2)
username_el.send_keys(USER_NAME)
time.sleep(2)
password_el.send_keys(PASSWORD)
submit_el = browser.find_element_by_css_selector("button[type='submit']")
time.sleep(1)
submit_el.click()

# resetting the "Save Login Details" page
time.sleep(5)
button_element = browser.find_element_by_css_selector("._6q-tv")
time.sleep(1)
button_element.click()
time.sleep(5)
button_element = browser.find_element_by_css_selector(
    "a.-qQT3:nth-child(1)"
)
time.sleep(1)
button_element.click()

time.sleep(5)
button_element = browser.find_element_by_css_selector(
    "li.Y8-fY:nth-child(3)")
button_element.click()
time.sleep(1)

