import json
from LK.tools.Json.path import Tools


class ConfigTools():

    # Корректный логин пользователя для входа
    @staticmethod
    def correct_login():
        return Tools.data['correct_login']

    # Корректный пароль пользователя для входа
    @staticmethod
    def correct_password():
        return Tools.data['correct_password']

    # Некорректный логин пользователя для входа
    @staticmethod
    def incorrect_login():
        return Tools.data['incorrect_login']

    # Некорректный пароль пользователя для входа
    @staticmethod
    def incorrect_password():
        return Tools.data['incorrect_password']

    # Текст ошибки при ошибки входа
    @staticmethod
    def login_error():
        return Tools.data['login_error']

    # Текст пользователя после входа в аватаре
    @staticmethod
    def name():
        return Tools.data['name']

    # Почта пользователя после входа в аватаре
    @staticmethod
    def email():
        return Tools.data['email']

    # Работник для смены в пользователя в графике работы
    @staticmethod
    def user():
        return Tools.data['user']

    # URL страницы входа пользователя
    @staticmethod
    def login_url():
        return Tools.data['login_url']

    # URL страницы графика работы пльзователя
    @staticmethod
    def grafik_url():
        return Tools.data['grafik_url']

    # URL страницы отчета пользователя
    @staticmethod
    def report_url():
        return Tools.data['report_url']
