class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://tt-develop.quality-lab.ru/login'
        self.browser.get(self.url)



