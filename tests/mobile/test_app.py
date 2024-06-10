import allure
from allure_commons.types import Severity

import cfg
from qa_guru_diplom.model.pages.android_app.authorization_page import authorization_page
from qa_guru_diplom.model.pages.android_app.external_browser import external_browser
from qa_guru_diplom.model.pages.android_app.general_page import general_page
from qa_guru_diplom.model.pages.android_app.welcome_screen import welcome_screen


@allure.tag("Android")
@allure.severity(Severity.NORMAL)
@allure.epic('Android')
class TestApp:

    @allure.feature('Authorization')
    @allure.title('Авторизация пользователя')
    def test_login(self):

        welcome_screen.skip()
        authorization_page.click_auth_button()
        authorization_page.tap_email_tab()
        authorization_page.type_email(cfg.user_email)
        authorization_page.type_password(cfg.user_password)
        authorization_page.click_enter_button()
        general_page.should_general_tab()

    @allure.feature('Welcome screen')
    @allure.title('Отображение заголовка на страницах')
    def test_welcome_screen(self):

        welcome_screen.should_text('Лучшие сериалы и фильмы мира собраны здесь')
        welcome_screen.click_next_page_button()
        welcome_screen.should_text('Смотрите сериалы')
        welcome_screen.click_next_page_button()
        welcome_screen.should_text('Получайте удовольствие от крутой озвучки')
        welcome_screen.click_start_button()
        authorization_page.should_title('Добро пожаловать!')

    @allure.feature('Site info')
    @allure.title('Переход на страницу "Документы правообладателей"')
    def test_copyright_docs(self):

        welcome_screen.skip()
        authorization_page.click_auth_button()
        authorization_page.click_copyright_docs_button()
        external_browser.should_url('https://flex-kino.com/copyright_docs/')