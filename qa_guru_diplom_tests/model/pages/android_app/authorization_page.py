from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class AuthorizationPage:
    def __init__(self):
        self.auth_button = browser.element((AppiumBy.ID, 'films.android:id/authBtn'))
        self.email_tab = browser.element((AppiumBy.ID, 'films.android:id/emailBtn'))
        self.email_input = browser.element((AppiumBy.ID, 'films.android:id/etEmailInput'))
        self.password_input = browser.element((AppiumBy.ID, 'films.android:id/etPasswordInput'))
        self.enter_button = browser.element((AppiumBy.ID, 'films.android:id/btnAction'))
        self.welcome_title = browser.element((AppiumBy.ID, 'films.android:id/welcome'))
        self.copyright_docs_button = browser.element((AppiumBy.ID, 'films.android:id/btnDocs'))

    def click_auth_button(self):
        with step('Нажать кнопку "Авторизация"'):
            self.auth_button.click()

    def tap_email_tab(self):
        with step('Нажать вкладку "Email"'):
            self.email_tab.click()

    def type_email(self, email):
        with step('Ввести Email'):
            self.email_input.type(email)

    def type_password(self, password):
        with step('Ввести пароль'):
            self.password_input.type(password)

    def click_enter_button(self):
        with step('Нажать кнопку "Войти"'):
            self.enter_button.click()

    def should_title(self, text):
        with step(f'На странице присутствует текст "{text}"'):
            self.welcome_title.should(have.text(text))

    def click_copyright_docs_button(self):
        with step('Нажать кнопку "Документы правообладателей"'):
            self.copyright_docs_button.click()


authorization_page = AuthorizationPage()
