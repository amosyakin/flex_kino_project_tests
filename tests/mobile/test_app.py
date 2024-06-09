import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic('Android')
@allure.title('Поиск на сайте Wikipedia')
def test_search():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'films.android:id/skipTv')).click()
