import allure
from selene import browser, have


class ContentPage:

    def __init__(self):
        self.content_title = browser.element('.serial-head__name')

    def should_content_title(self, content_name):
        with allure.step(f'На странице отображается заголовок с названием контента: {content_name}'):
            self.content_title.should(have.text(content_name))


content_page = ContentPage()
