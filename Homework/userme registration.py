from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнем формы и отправлем
    input_F_name = browser.find_element_by_css_selector("div.form-group.first_class > input")
    input_F_name.send_keys("Deny")

    input_L_name = browser.find_element_by_css_selector('div.form-group.second_class > input')
    input_L_name.send_keys("Kom")

    input_email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input_email.send_keys("kom@deny.ru")

    # Кликаем на кнопку
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()