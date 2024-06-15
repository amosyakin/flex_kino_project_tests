import allure
import pytest
from selene import browser
from appium import webdriver

import cfg
from qa_guru_diplom.utils.attach import mobile_attach_screen, mobile_attach_video


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            cfg.remote_url,
            options=cfg.to_driver_options()
        )
        browser.config.timeout = 60.0

    yield

    mobile_attach_screen()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    if cfg.context == 'bstack':
        mobile_attach_video(session_id)
