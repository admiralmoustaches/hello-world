from selenium import webdriver
import math
import time

browser = webdriver.Chrome("chromedriver")
link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    x = browser.find_element_by_id('treasure')
    z = x.get_attribute('valuex')
    y = calc(z)
    answr = browser.find_element_by_id("answer")
    answr.send_keys(y)
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_id('robotCheckbox_').click()
    bttn = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    bttn.click()
finally:
    time.sleep(15)
    browser.quit()