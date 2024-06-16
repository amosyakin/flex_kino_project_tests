import allure
from requests import Response

from qa_guru_diplom_tests.model.api.api_requests import api_request
from tests.api import conftest


def add_to_favorite(auth, endpoint_url, film_id) -> Response:
    url = endpoint_url + '/favorites/'
    body = {
        "films": film_id
    }
    cookie = auth.cookies

    with allure.step('Добавление фильма в избранное'):
        response = api_request("POST", url, json=body, cookie=cookie)

    return response


def get_favorites(auth, endpoint_url) -> Response:
    url = endpoint_url + '/favorites/'
    cookie = auth.cookies

    with allure.step('Получение списка'):
        response = api_request("GET", url,  cookie=cookie)

    return response


def delete_favorite_film(auth, endpoint_url, film_id):
    url = endpoint_url + f'/favorites/{film_id}/'
    cookie = auth.cookies

    with allure.step('Удаление из избранного'):
        response = api_request("DELETE", url, cookie=cookie)

    return response


def login(endpoint_url) -> Response:
    url = endpoint_url + '/login/'
    body = {
        "email": conftest.user_email,
        "password": conftest.user_password
    }
    with allure.step('Авторизация пользователя'):
        response = api_request("POST", url, json=body)

    return response


def get_site_info(endpoint_url):
    url = endpoint_url + '/site-info/'

    with allure.step('Получение списка приложений'):
        response = api_request("GET", url)

    return response
