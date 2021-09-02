import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from datetime import datetime
import allure
from LK.tools.Json.ConfigTools import ConfigTools

class CalendarPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        # блок с текстом, сообщающим текущий месяц и год
        self.grafik_text = lambda: self.browser.find_element(By.ID, 'schedule-month-title')

        # блоки с рабочим временем сотрудника
        self.green_day_text = lambda: self.browser.find_element(By.CLASS_NAME, 'fc-event-container')

        # блоки с выходными днями сотрудника
        self.day_off_text = lambda: self.browser.find_element(By.CLASS_NAME, 'fc-event-container')

        # поп-ап "Обновление календаря"
        self.calendar_wait =lambda: self.browser.find_element(By.XPATH, '//*[@id="schedule-overlay"]/span')

        # Календаря сотрудника
        self.calendar = lambda: self.browser.find_element(By.CSS_SELECTOR, "span.fc-title")

        # Кнопка календаря сотрудника
        self.button_calendar = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")

        self.button_calendar_submit = lambda: self.browser.find_element_by_xpath('// *[ @ id = "schedule-filters"] / form / div / div[4] / button')

        # Дата на сайте
        self.date = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")

        # Проверка полей календаря
        self.calendar_check = lambda: self.browser.find_elements_by_css_selector("span.fc-title")

        # поле справа от "Сотрудник", по клику выпадающий список
        self.sotrudnik_dropdown = lambda: \
            self.browser.find_element(By.ID, 'select2--container')

        # поле для ввода ФИО сотрудника
        self.sotrudnik_input = lambda: \
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[''2]/span/span/span[1]/input')

        # кнопка "Применить"
        self.primenit_button = lambda: \
            self.browser.find_element(By.XPATH, '//*[@id="schedule-filters"]/form/div/div[' '4]/button')


        # Кнопка смены месяца
        self.month_change = lambda: self.browser.find_element(By.XPATH,
                                            "//html/body/div[9]/div[2]/table/tbody/tr/td/span[10]")


    @allure.step('Переход на страницу календаря')
    def calendar_button(self):
        self.browser.get("https://tt-develop.quality-lab.ru/calendar/")
        return self

    @allure.step('Проверяю наличие рабочих дней в календаре')
    def check_workdays(self):
        try:
            self.grafik_text()
        except:
            self.is_exist(find=ConfigTools.data['work'],
                      where=self.green_day_text().text,
                      pass_text='Вижу рабочие дни в календаре',
                      fail_text='Не вижу рабочих дней в календаре')
        return self

    @allure.step('Проверяю наличие выходных дней в календаре')
    def check_day_off(self):
        try:
            self.day_off_text()
        except:
            self.is_exist(find=ConfigTools.data['holidays'],
                      where=self.day_off_text().text,
                      pass_text='Вижу выходные дни в календаре',
                      fail_text='Не вижу выходных дней в календаре')
        return self

    @allure.step('Ожидание загрузки календаря')
    def wait_calendar_button(self):
        self.wait_short.until(lambda browser: not self.calendar_wait().is_displayed())
        return self

    @allure.step('Проверяет соответствует ли месяц и год на странице с графиком истине')
    def check_month_and_year(self):
        expected = str(datetime.now().month) + str(datetime.now().year)
        try:
            self.grafik_text()
        except:
            self.is_exist(find=expected,
                        where=self.grafik_text().text,
                        pass_text='Месяц и год соответствуют ожидаемому',
                        fail_text='Месяц и год не соответствуют ожидаемым')
        return self

    @allure.step('Проверка смены месяца')
    def change_another_month(self):
        self.button_calendar().click()
        return self

    def button_another_month(self):
        self.month_change().click()
        return self

    def check_another_month(self):
        self.button_calendar_submit().click()
        return self

    @allure.step('Выбираю сотрудника')
    def choose_another_employee(self):
        self.sotrudnik_dropdown().click()
        self.sotrudnik_input().send_keys(ConfigTools.data['user'], Keys.ENTER)
        self.primenit_button().click()
        time.sleep(15)
        return self




