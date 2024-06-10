import allure
from allure_commons.types import Severity

from qa_guru_diplom.model.pages.web.footer import footer
from qa_guru_diplom.model.pages.web.general_page import general_page
from qa_guru_diplom.model.pages.web.page import page


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.epic("UI")
@allure.feature('Footer')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1212')
class TestFooter:

    @allure.title('Открытие страницы Документы правообладателей')
    def test_open_copyright(self, setup_browser):
        general_page.open()
        footer.scroll_to_footer()
        footer.click_button('Документы правообладателей')
        page.should_page_title('Документы правообладателей')

    @allure.title('Переход на страницу Android RuStore')
    def test_rustore_link(self, setup_browser):
        general_page.open()
        footer.scroll_to_footer()
        footer.click_app_icons('Rustore')
        page.should_url_redirect("https://www.rustore.ru/catalog/app/films.android")
