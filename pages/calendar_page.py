from datetime import datetime as dt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from datetime import datetime
import allure
from LK.tools.Json.ConfigTools import ConfigTools


class CalendarPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        # поп-ап "Обновление календаря"
        self.calendar_pop_up = lambda: self.browser.find_element(By.XPATH, '//*[@id="schedule-overlay"]/span')

        # рабочие дни в календаре
        self.schedule_working_days = lambda: self.browser.find_elements_by_css_selector(
            ".schedule-badge--default")

        # нерабочие дни в календаре
        self.schedule_non_working_days = lambda: self.browser.find_elements_by_css_selector(
            ".schedule-badge--no-event")

        # Календарь сотрудника
        self.calendar = lambda: self.browser.find_element(By.CSS_SELECTOR, "span.fc-title")

        # Кнопка выбора месяца сотрудника
        self.button_calendar = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div/form/div/div[3]/div/span/i")

        # Кнопка выбора месяца "Принять"
        self.button_calendar_submit = lambda: self.browser.find_element_by_xpath(
            '// *[ @ id = "schedule-filters"] / form / div / div[4] / button')

        # Дата на сайте
        self.date = lambda: self.browser.find_element_by_xpath(
            ".//html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/h3")

        # Проверка полей календаря
        self.calendar_check = lambda: self.browser.find_elements_by_css_selector("span.fc-title")

        # поле справа от "Сотрудник", по клику выпадающий список
        self.dropdown_employers = lambda: \
            self.browser.find_element(By.ID, 'select2--container')

        # поле для ввода ФИО сотрудника
        self.input_employers = lambda: \
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[''2]/span/span/span[1]/input')

        # кнопка "Применить" для выбора струдника
        self.submit_button_employers = lambda: \
            self.browser.find_element(By.XPATH, '//*[@id="schedule-filters"]/form/div/div[' '4]/button')

        # Кнопка смены месяца
        self.month_change = lambda: self.browser.find_element(By.XPATH,
                                                              "//html/body/div[9]/div[2]/table/tbody/tr/td/span[10]")

    # Ячейки календаря с датами этих ячеек
    __current_cell_locator__ = '//div[contains(@class, "fc-content-skeleton")]/table/thead/tr/td'

    # Аттрибут, где лежит дата в ячейке
    __cell_date_attr__ = "data-date"

    # Ячейки календаря с первой частью дня в расписании
    __first_half_of_day_in_cell_locator__ = '//div[contains(@class, "fc-content-skeleton")]/table/tbody/tr[1]/td'

    # Аттрибут количества ячеек, у выходных равен двум, у рабочих дней отсутствует
    __weekend_attr__ = "rowspan"

    @allure.step('Переход на страницу календаря')
    def calendar_button(self):
        self.browser.get(ConfigTools.grafik_url())
        return self

    @allure.step('Ожидание поп-ап "Ожидание календаря"')
    def wait_calendar_button(self):
        self.wait_short.until(lambda browser: not self.calendar_pop_up().is_displayed())
        return self

    @allure.step('Проверяет соответствует ли месяц и год на странице с графиком работника')
    def check_month_and_year(self):
        assert self.date().text == datetime.now().strftime('%d.%m.%y')
        return self

    @allure.step('Кликаем кнопку выбора месяца')
    def change_another_month(self):
        self.button_calendar().click()
        return self

    @allure.step('Кликаем месяц')
    def button_another_month(self):
        self.month_change().click()
        return self

    @allure.step('Кликаем кнопку календаря "Применить"')
    def check_another_month(self):
        self.button_calendar_submit().click()
        return self

    @allure.step('Выбираю сотрудника')
    def choose_another_employee(self):
        self.dropdown_employers().click()
        self.input_employers().send_keys(ConfigTools.user(), Keys.ENTER)
        self.submit_button_employers().click()
        return self

    def get_working_days_list(self, offset: int = 0):
        """Получение списка рабочих дней в месяце в виде списка"""
        current_month = BasePage.normalize(offset)[0]
        i = 0
        current_month_list = []
        # Пробегаемся по всем ячейкам и берём из них даты, чтобы не учитывать даты не в этом месяце
        for td in self.browser.find_elements_by_xpath(self.__current_cell_locator__):
            attr = td.get_attribute(self.__cell_date_attr__)
            if attr is None:
                continue
            # В атрибуте data-date указана дата в формате 2021-09-01, мы отсюда берём только 09
            if current_month == int(attr[9]):
                current_month_list.append(i)
            i += 1
        return current_month_list

    def get_working_days_stat(self, offset: int = 0):
        """Получение количества рабочих и нерабочих дней"""
        days, weekends, workdays = (0, 0, 0)
        # Получаем список рабочих дней
        current_month_list = self.get_working_days_list(offset)
        for td in self.browser.find_elements_by_xpath(self.__first_half_of_day_in_cell_locator__):
            if days not in current_month_list:
                days += 1
                continue
            attr_rowspan = td.get_attribute(self.__weekend_attr__)
            if attr_rowspan is not None:
                weekends += 1
            else:
                workdays += 1
            days += 1
        return days, workdays, weekends
