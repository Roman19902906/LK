import os
import configparser
import pytest
from selenium import webdriver
# from login.pages.login_page import LoginPage
import allure
import requests

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
    # os.environ['URL'] = 'https://tt-develop1.quality-lab.ru'
    link = os.getenv('URL', default='https://tt-develop.quality-lab.ru/login')
    browser = webdriver.Chrome()
    browser.get(link)
    print("\nstart browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def auth(browser):
    # with allure.step("Авторизация"):
    # with allure.step("Логин Авто Пользователь"):
    # input1 = browser.find_element(*LoginPage.USERNAME)
    # input1.send_keys(config.get('User', "login"))
    # with allure.step("Пароль 12345678"):
    # input2 = browser.find_element(*LoginPage.PASSWORD)
    # input2.send_keys(config.get('User', "password"))
    # with allure.step("Вход"):
    # button = browser.find_element(*LoginPage.BUTTON)
    # button.click()
    # yield browser
    #browser = webdriver.Chrome()
    #url = "https://tt-develop.quality-lab.ru/login"
    #browser.get(url)
    request_cookies_browser = browser.get_cookies()
    datasa = {"_csrf_token": " ", "_username": "Авто пользователь",
              "_password": "12345678", "_submit": "Войти"}
    l = requests.Session()
    [l.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
    l.post("https://tt-develop.quality-lab.ru/login_check", datasa)
    dict_resp_cookies = l.cookies.get_dict()
    response_cookies_browser = [{"name": name, "value": value} for name, value in
                                dict_resp_cookies.items()]
    l.close()
    [browser.add_cookie(c) for c in response_cookies_browser]
    browser.get("https://tt-develop.quality-lab.ru/login")
    yield browser


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
