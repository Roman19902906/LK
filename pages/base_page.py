from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from LK.tools.Json.ConfigTools import ConfigTools
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

        # блоки с рабочими днями сотрудника
        self.check_workdays = lambda: self.browser.find_elements(By.CSS_SELECTOR,
                                                             'a.fc-day-grid-event fc-h-event fc-event fc-start fc-end schedule-badge schedule-badge--block schedule-badge--default schedule-badge--')

        # блоки с выходными днями сотрудника
        self.check_holidays = lambda: self.browser.find_elements(By.CSS_SELECTOR,
                                                             'a.fc-day-grid-event fc-h-event fc-event fc-start fc-end schedule-badge schedule-badge--block schedule-badge--no-event schedule-badge--')
    login_url = ConfigTools.login_url
    grafik_url = ConfigTools.grafik_url
    otchet_url = ConfigTools.report_url

    @property
    def wait_short(self):
        return WebDriverWait(self.browser, 15)

    def is_exist(self, find, where, pass_text, fail_text):
        """
        Считает наличие искомого в элементе успехом.
        :param self:
        :param find: что ищем
        :param where: где ищем
        :param pass_text: текст в случае успеха
        :param fail_text: текст в случае ошибки
        """

    def is_not_exist(self, find, where, pass_text, fail_text):
        """
        Cчитает отсутствие искомого в элементе успехом.
        :param self:
        :param find: что ищем
        :param where: где ищем
        :param pass_text: текст в случае успеха
        :param fail_text: текст в случае ошибки
        """

    def check_exists_workdays(self):
        try:
            self.check_workdays()
        except NoSuchElementException:
            return False
        return True

    def check_exists_holidays(self):
        try:
            self.check_holidays()
        except NoSuchElementException:
            return False
        return True


