import allure
from requests import Response

import cfg
from qa_guru_diplom.model.api.api_requests import post_request, get_request, delete_request


def add_to_favorite(auth, endpoint_url, film_id) -> Response:
    url = endpoint_url + '/favorites/'
    body = {
        "films": film_id
    }
    cookie = auth.cookies

    with allure.step('Добавление фильма в избранное'):
        response = post_request(url, body, cookies=cookie)

    return response


def get_favorites(auth, endpoint_url) -> Response:
    url = endpoint_url + '/favorites/'
    cookie = auth.cookies

    with allure.step('Получение списка'):
        response = get_request(url, cookies=cookie)

    return response


def delete_favorite_film(auth, endpoint_url, film_id):
    url = endpoint_url + f'/favorites/{film_id}/'
    cookie = auth.cookies

    with allure.step('Удаление из избранного'):
        response = delete_request(url, cookies=cookie)

    return response


def login(endpoint_url) -> Response:
    url = endpoint_url + '/login/'
    body = {
        "email": cfg.user_email,
        "password": cfg.user_password
    }
    with allure.step('Авторизация пользователя'):
        response = post_request(url, body)

    return response


def get_site_info(endpoint_url):
    url = endpoint_url + '/site-info/'

    with allure.step('Получение списка приложений'):
        response = get_request(url)

    return response
