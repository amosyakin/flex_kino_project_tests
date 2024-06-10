from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class GeneralPage:
    def __init__(self):
        self.navigation_tabs = browser.element((AppiumBy.ID, 'films.android:id/general_graph'))

    def should_general_tab(self):
        with step(f'На странице присутсвует вкладка "Главная"'):
            self.navigation_tabs.should(have.attribute('content-desc', 'Главная'))


general_page = GeneralPage()
