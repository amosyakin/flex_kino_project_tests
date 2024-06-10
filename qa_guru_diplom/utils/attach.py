import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response
from selene import browser

import cfg


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = f"https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def response_log(response: Response):
    logging.info("Request URL: " + response.request.url)
    if response.request.body:
        request_body = response.request.body
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        logging.info("Request body: " + request_body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Request cookies: " + str(response.cookies))
    logging.info("Status code: " + str(response.status_code))


def add_api_attach(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        request_body = response.request.body
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        allure.attach(
            body=json.dumps(json.loads(request_body), indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )


def mobile_attach_screen():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )


def mobile_attach_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(cfg.bstack_userName, cfg.bstack_accessKey),
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
