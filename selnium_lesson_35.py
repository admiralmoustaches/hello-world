from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    FirstName = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    FirstName.send_keys('Roman')
    LastName = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    LastName.send_keys('Nikolaev')
    Email = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    Email.send_keys('admiralmoustache@yandex.ru')
    Phone = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    Phone.send_keys('+79117810500')
    Adress = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    Adress.send_keys('Spb prkt Vetranov d 76 kv 169')
    # Отправляем заполненную форму


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()