from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


browser = webdriver.Chrome('chromedriver')
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.implicitly_wait(1)
try:
    browser.get(link)
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    browser.find_element_by_class_name('btn.btn-primary').click()
    def doTheMath():
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        value = browser.find_element_by_id('input_value').text
        print(value)
        x = calc(value)
        print(x)
        browser.find_element_by_id('answer').send_keys(x)
        browser.find_element_by_id('solve').click()

    doTheMath()

finally:
    time.sleep(10)
    browser.quit()