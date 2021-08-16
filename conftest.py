import pytest
import time
from selenium import webdriver
from login.pages.login_page import LoginPage


@pytest.yield_fixture(scope="function", autouse=True)
def start_fun():
    print("\ntest start")
    yield
    print("\ntest finished")


@pytest.yield_fixture(scope="class", autouse=True)
def start_fun1():
    print("\nFirstTest class started")
    yield
    print("\nAll tests in FirstTest finished")


@pytest.fixture(scope="function")
def browser():
    link = 'https://tt-develop.quality-lab.ru/login'
    browser = webdriver.Chrome()
    browser.get(link)
    print("\nstart browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def auth(browser):
    input1 = browser.find_element(*LoginPage.USERNAME)
    input1.send_keys("Авто Пользователь")
    input2 = browser.find_element(*LoginPage.PASSWORD)
    input2.send_keys("12345678")
    button = browser.find_element(*LoginPage.BUTTON)
    button.click()
    yield browser
