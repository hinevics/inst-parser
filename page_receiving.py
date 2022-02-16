from typing import List
import time

from selenium import webdriver

from config import PATH_GECKODRIVER, USER_NAME, PASSWORD, URL_USER

# Request for access
print('LOG:\tSTART OPEN PAGE {url}'.format(url=URL_USER))
browser = webdriver.Firefox(executable_path=PATH_GECKODRIVER)
browser.get(URL_USER)
time.sleep(2)
username_el = browser.find_element_by_name('username')
password_el = browser.find_element_by_name('password')
print('LOG:\t -OK-')
print('-' * 10)

# login
print('LOG:\t-START LOGIN-')
time.sleep(2)
username_el.send_keys(USER_NAME)
time.sleep(2)
password_el.send_keys(PASSWORD)
submit_el = browser.find_element_by_css_selector("button[type='submit']")
time.sleep(1)
submit_el.click()
print('LOG:\t -OK-')
print('-' * 10)

# resetting the "Save Login Details" page
# 1
print('LOG:\t-RESETTING-')
time.sleep(5)
button_element = browser.find_element_by_css_selector("._6q-tv")
time.sleep(1)
button_element.click()
time.sleep(5)
print('LOG:\t -OK-')
print('-' * 10)

# 2
print('LOG:\t-OPEN PROFILE-')
button_element = browser.find_element_by_css_selector(
    "a.-qQT3:nth-child(1)"
)
time.sleep(1)
button_element.click()
time.sleep(5)
print('LOG:\t -OK-')
print('-' * 10)


# search for followers
def search_followers(browser: webdriver.Firefox) -> List[str]:
    print('-START SEARCH FOLLOWERS-')
    button_element = browser.find_element_by_css_selector(
        "li.Y8-fY:nth-child(3)")
    button_element.click()
    time.sleep(1)
    elements = browser.find_element_by_class_name('PZuss')
    elements = elements.find_element_by_tag_name('li')
    print(elements.)

    print('LOG:\t -OK-')
    print('-' * 10)


def main():
    search_followers(browser=browser)


if __name__ == "__main__":
    main()
