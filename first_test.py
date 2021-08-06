import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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


class TestFirst():
    def test_1(start_fun):
        print('Тест №1')
        pytest.assume(2 + 2 == 4)

    def test_2(start_fun):
        print('Тест №2')
        pytest.assume(2 + 2 == 5)

    def test_3(start_fun):
        print('Тест №3')
        pytest.assume(2 + 2 == 4)

    def test_4(start_fun):
        print('Тест №3')
        pytest.assume(1 / 0 == 1)

    def test_5(start_fun):
        print('Тест №5')


class TestLogin:
    def test_initWebDriver(self):
        browser = webdriver.Chrome()
        browser.get("https://tt-develop.quality-lab.ru")
        options = Options()
        options.add_argument("--window-size=500x500")
        browser.set_window_size(200, 100)
        browser.maximize_window()
        browser.quit()
