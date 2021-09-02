from selenium.webdriver.support.wait import WebDriverWait
import os
from LK.tools.Json.ConfigTools import ConfigTools

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    login_url = os.path.join(ConfigTools.data['project_url'], 'login')
    grafik_url = os.path.join(ConfigTools.data['project_url'], 'calendar')
    otchet_url = os.path.join(ConfigTools.data['project_url'], 'report/group/edit')

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
