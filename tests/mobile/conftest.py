import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from appium import webdriver

import config
from flex_kino_project_tests.utils.attach import mobile_attach_screen, mobile_attach_video


load_dotenv()

user_email = os.getenv('USER_EMAIL')
user_password = os.getenv('USER_PASSWORD')


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=config.to_driver_options()
        )
        browser.config.timeout = 60.0

    yield

    mobile_attach_screen()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    if config.context == 'bstack':
        mobile_attach_video(session_id)
