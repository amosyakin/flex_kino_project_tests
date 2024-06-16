import requests

from flex_kino_project_tests.utils.attach import add_api_attach, response_log


def api_request(method, url, json=None, params=None, cookie=None):
    response = requests.request(method, url, json=json, params=params, cookies=cookie)
    response_log(response)
    add_api_attach(response)

    return response
