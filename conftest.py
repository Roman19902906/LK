import os

import pytest
from selenium import webdriver
import allure
import requests



@pytest.fixture(scope="function")
def browser():
    os.environ['URL'] = 'https://tt-develop.quality-lab.ru'
    link = os.getenv('URL', default=None)
    browser = webdriver.Chrome()
    browser.get(link)
    print("\nstart browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def auth(browser):
    request_cookies_browser = browser.get_cookies()
    datas = {"_csrf_token": " ", "_username": "Авто пользователь",
             "_password": "12345678", "_submit": "Войти"}
    sessionauth = requests.Session()
    [sessionauth.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
    sessionauth.post("https://tt-develop.quality-lab.ru/login_check", datas)
    dict_resp_cookies = sessionauth.cookies.get_dict()
    response_cookies_browser = [{"name": name, "value": value} for name, value in
                                dict_resp_cookies.items()]
    sessionauth.close()
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
