from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver')

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(link)
    elements = browser.find_elements_by_tag_name('input')
    for el in elements:
        el.send_keys('MY ANSWER')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.close()