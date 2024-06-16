import allure
from selene import browser, by, have


class Header:

    def __init__(self):
        self.header_menu = browser.element('.header .menu')
        self.search_icon = browser.element('.header .search')
        self.search_input = browser.element('.search-input__control')
        self.search_result = browser.element('.search__result')
        self.empty_search_result = browser.element('.search__empty')
        self.profile_avatar = browser.element('.profile__image')
        self.profile_email = browser.all('.user-profile__login')

    def click_menu(self, menu_name):
        with allure.step('В хедере перейти в раздел {menu}'):
            self.header_menu.element(by.text(menu_name)).click()

    def click_search_button(self):
        with allure.step('Нажать на иконку "Поиск"'):
            self.search_icon.click()

    def type_content_to_search(self, content_name):
        with allure.step(f'Ввести название контента "{content_name}" '):
            self.search_input.type(content_name)

    def click_found_content(self, content_name):
        with allure.step(f'Перейти по найденному контенту: "{content_name}" '):
            self.search_result.element(by.text(content_name)).click()

    def should_search_content(self, content_name):
        with allure.step(f'В результатах поиска отображается фильм: {content_name}'):
            self.search_result.should(have.text(content_name))

    def should_empty_search_result(self):
        with allure.step(f'В результатах поиска отображается текст: "К сожалению, ничего не найдено"'):
            self.empty_search_result.should(have.text('К сожалению, ничего не найдено.'))

    def hover_profile_avatar(self):
        with allure.step('Раскрыть профиль'):
            self.profile_avatar.hover()

    def should_profile_email(self, email):
        with allure.step(f'В Профиле отображается E-mail пользователя: {email}'):
            self.profile_email.should(have.texts(email))


header = Header()
