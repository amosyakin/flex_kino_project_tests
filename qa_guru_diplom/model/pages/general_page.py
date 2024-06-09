import allure
from selene import browser


class GeneralPage:
    def open(self):
        with allure.step('Открытие главной страницы'):
            browser.open('/')
            return self


general_page = GeneralPage()
