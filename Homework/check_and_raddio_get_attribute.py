from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = ('http://suninjuly.github.io/get_attribute.html')
    browser = webdriver.Chrome()
    browser.get(link)

    x_val = browser.find_element_by_id('treasure')
    valuex_at = x_val.get_attribute("valuex")
    print("valuex Yes: ", valuex_at)
    assert valuex_at is not None, "Not valuex"

    x = valuex_at
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    input_checkbox = browser.find_element_by_id('robotCheckbox')
    input_checkbox.click()

    input_raddiobutton = browser.find_element_by_id('robotsRule')
    input_raddiobutton.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(6)
    browser.quit()