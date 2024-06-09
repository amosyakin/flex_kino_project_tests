import allure
from selene import browser, command, by


class Footer:

    def __init__(self):
        self.footer = browser.element('.footer')
        self.footer_menu = browser.element('.menu-button')
        self.app_icon = browser.element('.footer__applications')

    def scroll_to_footer(self):
        with allure.step('Пролистать до футера'):
            self.footer.perform(command.js.scroll_into_view)

    def click_button(self, button_name):
        with allure.step(f'Нажать на кнопку "{button_name}"'):
            self.footer_menu.element(by.text(button_name)).click()

    def click_app_icons(self, app_name):
        with allure.step(f'Нажать на кнопку "{app_name}"'):
            self.app_icon.element(f'img[alt*="{app_name}"]').perform(command.js.click)


footer = Footer()
