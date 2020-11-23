from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = ('http://suninjuly.github.io/explicit_wait2.html')
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element_by_id('book').click()


    num_x = browser.find_element_by_id('input_value')
    x = num_x.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button1 = browser.find_element_by_id('solve')
    button1.click()

finally:
    time.sleep(3)
    browser.quit()