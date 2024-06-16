import allure
from selene import browser


class LoginPage:

    def __init__(self):
        self.auth_type_tab = browser.element('.register__through')
        self.email_input = browser.element('input[type = "email"]')
        self.password_input = browser.element('input[type = "password"]')
        self.login_button = browser.element('button[type = "submit"]')

    def open(self):
        with allure.step('Открытие страницы авторизации'):
            browser.open('/login')
            return self

    def click_auth_type_tab(self, auth_type):
        with allure.step(f'Выбрать вкладку {auth_type}'):
            self.auth_type_tab.element(f"//a[text()='{auth_type}']").click()

    def type_email(self, email):
        with allure.step(f'Ввести email'):
            self.email_input.type(email)

    def type_password(self, password):
        with allure.step(f'Ввести пароль'):
            self.password_input.type(password)

    def click_login_button(self):
        with allure.step(f"Нажать кнопку 'Войти'"):
            self.login_button.click()


login_page = LoginPage()
