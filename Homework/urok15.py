from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



try:
    link = ('http://suninjuly.github.io/selects1.html')
    browser = webdriver.Chrome()
    browser.get(link)

    num1_at = browser.find_element_by_id('num1')
    num1 = num1_at.text
    print("valuex Yes: ", num1)
    assert num1 is not None, "Not valuex"

    num2_at = browser.find_element_by_id('num2')
    num2 = num2_at.text
    print("Yes: ", num2)
    assert num2 is not None, "Not "

    x = int(num1) + int(num2)
    print(x)

    str_sum = Select(browser.find_element_by_tag_name('select'))
    str_sum.select_by_value(str(x))

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(3)
    browser.quit()

