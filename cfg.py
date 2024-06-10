import os
from pathlib import Path

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from qa_guru_diplom import utils

context = os.getenv('context', 'bstack')
load_dotenv(Path(f'.env.{context}'))
# load_dotenv()

user_email = os.getenv('USER_EMAIL')
user_password = os.getenv('USER_PASSWORD')

domain_url = os.getenv('DOMAIN_URL')
api_v = os.getenv('API_V')

film_id = os.getenv('FILM_ID')

remote_url = os.getenv('REMOTE_URL')
deviceName = os.getenv('DEVICE_NAME')
udid = os.getenv('UDID')
app = os.getenv('APP')
bstack_userName = os.getenv('BSTACK_USER_NAME')
bstack_accessKey = os.getenv('BSTACK_ACCESSKEY')

if not app:
    raise ValueError("The 'app' environment variable is not set or is empty")


def to_driver_options():
    options = UiAutomator2Options()

    if context == 'device' or context == 'emulator':
        options.set_capability('udid', udid)
        options.set_capability('remote_url', remote_url)
        options.set_capability('app', utils.file.abs_path_from_project(app))

    if context == 'bstack':
        options.set_capability('platformVersion', '9.0')
        options.set_capability('app', app)
        options.set_capability('deviceName', deviceName)
        options.set_capability('remote_url', remote_url)
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options
