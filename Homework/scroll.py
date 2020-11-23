from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = ('http://SunInJuly.github.io/execute_script.html')
    browser = webdriver.Chrome()
    browser.get(link)

    x_num = browser.find_element_by_id('input_value')
    x = x_num.text
    print('Yes:', x)
    assert x is not None, "NOT"

    browser.execute_script("window.scrollBy(0, 100);")

    y = calc(x)
    print(y)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    input_box = browser.find_element_by_id('robotCheckbox')
    input_box.click()

    input_rad = browser.find_element_by_id('robotsRule')
    input_rad.click()
    
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(3)
    browser.quit()