import allure
from allure_commons.types import Severity

from qa_guru_diplom_tests.model.pages.web.content_page import content_page
from qa_guru_diplom_tests.model.pages.web.general_page import general_page
from qa_guru_diplom_tests.model.pages.web.header import header


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.epic("UI")
@allure.feature('Search')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1259')
class TestSearch:

    @allure.title('Выполнить поиск по контенту')
    @allure.id("32845")
    def test_search_by_content(self, setup_browser):
        general_page.open()
        header.click_search_button()
        header.type_content_to_search('Оппенгеймер')
        header.should_search_content('Оппенгеймер')

    @allure.id("32950")
    @allure.title('Переход по найденному контенту в карточку контента')
    def test_open_found_content(self, setup_browser):
        general_page.open()
        header.click_search_button()
        header.type_content_to_search('Оппенгеймер')
        header.click_found_content('Оппенгеймер')
        content_page.should_content_title('Оппенгеймер')

    @allure.id("32951")
    @allure.title('Отображение страницы с пустым результатом поиска')
    def test_empty_search_result(self, setup_browser):
        general_page.open()
        header.click_search_button()
        header.type_content_to_search('12345678')
        header.should_empty_search_result()
