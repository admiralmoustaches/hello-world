from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome("chromedriver")
link = 'http://suninjuly.github.io/selects2.html'


try:
    browser.get(link)
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    z = int(x)+int(y)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(z))
    bttn = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    bttn.click()
finally:
    time.sleep(15)
    browser.quit()