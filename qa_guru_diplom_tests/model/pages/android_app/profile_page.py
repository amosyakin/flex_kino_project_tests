from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ProfilePage:
    def __init__(self):
        self.email_info = browser.element((AppiumBy.ID, 'films.android:id/emailEt'))

    def should_email_info(self, email):
        with step(f'В профиле отображается email авторизованного пользователя: {email}'):
            self.email_info.should(have.text(email))


profile_page = ProfilePage()
