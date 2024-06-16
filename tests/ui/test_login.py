import allure
from allure_commons.types import Severity

from qa_guru_diplom_tests.model.pages.web.header import header
from qa_guru_diplom_tests.model.pages.web.login_page import login_page
from tests.ui import conftest


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.epic("UI")
@allure.feature('Authorization')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1259')
@allure.title("Авторизация пользователя")
@allure.id("32949")
def test_login(setup_browser):
    login_page.open()
    login_page.click_auth_type_tab('E-mail')
    login_page.type_email(conftest.user_email)
    login_page.type_password(conftest.user_password)
    login_page.click_login_button()
    header.hover_profile_avatar()
    header.should_profile_email(conftest.user_email)
