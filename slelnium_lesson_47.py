import time
from selenium import webdriver
import math
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty.txt')

browser =  webdriver.Chrome('chromedriver')
link =  "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
     browser.find_element_by_name('firstname').send_keys('22')
     browser.find_element_by_name('lastname').send_keys('22')
     browser.find_element_by_name('email').send_keys('22')
     browser.find_element_by_id('file').send_keys(file_path)
     browser.find_element_by_xpath("//button[@class='btn btn-primary']")

finally:
    time.sleep(10)
    browser.quit()