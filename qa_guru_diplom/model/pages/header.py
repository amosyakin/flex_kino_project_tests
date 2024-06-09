import allure
from selene import browser, by, have


class Header:

    def __init__(self):
        self.header_menu = browser.element('.header .menu')
        self.search_icon = browser.element('.header .search')
        self.search_input = browser.element('.search-input__control')
        self.search_result = browser.element('.search__result')

    def click_menu(self, menu_name):
        with allure.step('В хэдэре перейти в раздел {menu}'):
            self.header_menu.element(by.text(menu_name)).click()

    def click_search_button(self):
        with allure.step('Нажать на иконку "Поиск"'):
            self.search_icon.click()

    def type_content_to_search(self, content_name):
        with allure.step(f'Ввести название контента "{content_name}" '):
            self.search_input.type(content_name)

    def should_search_content(self, content_name):
        self.search_result.should(have.text(content_name))


header = Header()
