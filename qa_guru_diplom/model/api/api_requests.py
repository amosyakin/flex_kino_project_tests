import requests

from qa_guru_diplom.utils.attach import add_api_attach, response_log


def get_request(url, **kwargs):
    response = requests.get(url=url, **kwargs)

    response_log(response)
    add_api_attach(response)
    return response


def post_request(url, body, **kwargs):
    response = requests.post(url=url, json=body, **kwargs)

    response_log(response)
    add_api_attach(response)
    return response


def delete_request(url, **kwargs):
    response = requests.delete(url=url, **kwargs)

    response_log(response)
    add_api_attach(response)
    return response
