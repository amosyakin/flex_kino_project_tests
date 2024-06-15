from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class WelcomeScreen:
    def __init__(self):
        self.skip_button = browser.element((AppiumBy.ID, 'films.android:id/skipTv'))
        self.next_button = browser.element((AppiumBy.ID, 'films.android:id/nextTv'))
        self.title = browser.element((AppiumBy.ID, 'films.android:id/mainTv'))
        self.start_button = browser.element((AppiumBy.ID, 'films.android:id/startBtn'))

    def skip(self):
        with step('Нажать кнопку "Пропустить"'):
            self.skip_button.click()

    def click_next_page_button(self):
        with step('Нажать кнопку "Далее"'):
            self.next_button.click()

    def should_text(self, text):
        with step(f'На странице присутствует текст "{text}"'):
            self.title.should(have.text(text))

    def click_start_button(self):
        with step('Нажать кнопку "Начать"'):
            self.start_button.click()


welcome_screen = WelcomeScreen()
