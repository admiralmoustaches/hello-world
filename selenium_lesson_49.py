import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome("chromedriver")
link = 'http://suninjuly.github.io/alert_accept.html'


try:
    browser.get(link)
    browser.find_element_by_class_name('btn.btn-primary').click()
    browser.switch_to.alert.accept()
    value = browser.find_element_by_id('input_value').text
    x = calc(value)
    browser.find_element_by_class_name('form-control').send_keys(x)
    browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
finally:
    time.sleep(10)
    browser.quit()