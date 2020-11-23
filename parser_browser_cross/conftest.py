import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or yandex")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "yandex":
        print("\nstart yandex browser for test..")
        browser = webdriver.Chrome("yandexdriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome or yandex")
    yield browser
    print("\nquit browser..")
    browser.quit()
