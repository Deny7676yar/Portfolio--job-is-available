from selenium import webdriver
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = ('http://suninjuly.github.io/alert_accept.html')
    browser = webdriver.Chrome()
    browser.get(link)

    but = browser.find_element_by_css_selector('button.btn')
    but.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num_x = browser.find_element_by_id('input_value')
    x = num_x.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
