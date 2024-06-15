import os
from pathlib import Path

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from qa_guru_diplom_tests import utils

context = os.getenv('context', 'bstack')
load_dotenv(Path(f'.env.{context}'))

remote_url = os.getenv('REMOTE_URL')
deviceName = os.getenv('DEVICE_NAME')
udid = os.getenv('UDID')
app = os.getenv('APP')
appWaitActivity = 'films.android.*'
bstack_userName = os.getenv('BSTACK_USER_NAME')
bstack_accessKey = os.getenv('BSTACK_ACCESSKEY')


def to_driver_options():
    options = UiAutomator2Options()

    if context == 'device' or context == 'emulator':
        options.set_capability('udid', udid)
        options.set_capability('appWaitActivity', appWaitActivity)
        options.set_capability('remote_url', remote_url)
        options.set_capability('app', utils.file.abs_path_from_project(app))

    if context == 'bstack':
        options.set_capability('platformVersion', '13.0')
        options.set_capability('app', app)
        options.set_capability('appWaitActivity', appWaitActivity)
        options.set_capability('deviceName', deviceName)
        options.set_capability('remote_url', remote_url)
        options.set_capability('adbExecTimeout', 60000)
        options.set_capability(
            'bstack:options', {
                'projectName': 'QA GURU Diplom',
                'buildName': 'Flex Android App',
                'sessionName': 'BStack session',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options
