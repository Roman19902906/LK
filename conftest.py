import os
import configparser
import pytest
from selenium import webdriver
from login.pages.login_page import LoginPage
import allure

config = configparser.ConfigParser()
config.read('settings.ini')
config.get('User', "password")
config.get('User', "login")


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
    #os.environ['URL'] = 'https://tt-develop1.quality-lab.ru'
    link = os.getenv('URL', default='https://tt-develop.quality-lab.ru/login')
    browser = webdriver.Chrome()
    browser.get(link)
    print("\nstart browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()


#import configparser

#config = configparser.ConfigParser()
#config.read('example.ini')
#a = config.get('User', "password")

@pytest.fixture(scope="function")
def auth(browser):
    with allure.step("Авторизация"):
        with allure.step("Логин Авто Пользователь"):
            input1 = browser.find_element(*LoginPage.USERNAME)
            input1.send_keys(config.get('User', "login"))
        with allure.step("Пароль 12345678"):
            input2 = browser.find_element(*LoginPage.PASSWORD)
            input2.send_keys(config.get('User', "password"))
        with allure.step("Вход"):
            button = browser.find_element(*LoginPage.BUTTON)
            button.click()
        yield browser
