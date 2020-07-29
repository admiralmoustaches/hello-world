import time
from selenium import webdriver
import math

browser = webdriver.Chrome('chromedriver')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser.get(link)
    browser.find_element_by_class_name('trollface.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value = browser.find_element_by_id('input_value').text
    x = calc(value)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_class_name('btn.btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()

