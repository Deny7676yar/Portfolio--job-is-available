from selenium import webdriver
import time
import os

try:
    link = ('http://suninjuly.github.io/file_input.html')
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(2)')
    input1.send_keys('Deny')

    input2 = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(4)')
    input2.send_keys('Kom')

    input3 = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(6)')
    input3.send_keys('emal@qe')

    element = browser.find_element_by_id('file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '123.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(3)
    browser.quit()