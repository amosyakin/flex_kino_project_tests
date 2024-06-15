from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ExternalBrowser:
    def __init__(self):
        self.url_bar = browser.element((AppiumBy.ID, 'com.android.chrome:id/url_bar'))

    def should_url(self, url):
        with step(f"Открылась страница по адресу '{url}'"):
            self.url_bar.should(have.text(url))


external_browser = ExternalBrowser()
