from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class PermissionController:
    def __init__(self):
        self.permission_allow = browser.element(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button'))

    def click_allow_button(self):
        with step('Разрешение на получение уведомлений в приложении'):
            self.permission_allow.click()


permission_controller = PermissionController()
