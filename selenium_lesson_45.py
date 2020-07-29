import time
from selenium import webdriver
import math
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser =  webdriver.Chrome('chromedriver')
link =  "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    value = browser.find_element_by_id('input_value').text
    z = calc(value)
    browser.find_element_by_id('answer').send_keys(z)
    browser.find_element_by_id('robotCheckbox').click()
    inv = browser.find_element_by_id("robotsRule")
    browser.execute_script('return arguments[0].scrollIntoView(true);',inv)
    inv.click()
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
finally:
    time.sleep(10)
    browser.quit()