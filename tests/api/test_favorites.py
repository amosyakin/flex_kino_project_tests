import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate

import cfg
from qa_guru_diplom.model.api import api
from qa_guru_diplom.schemas.favorites import post_favorites, get_favorites


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.epic('API')
@allure.feature('Favorites')
class TestFavorites:

    @allure.title('Добавление в избранное фильма')
    def test_add_favorite(self, auth, endpoint_url):
        film_id = cfg.film_id
        response = api.add_to_favorite(auth, endpoint_url, film_id)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 201

        with allure.step('Валидация JSON-схемы'):
            response_json_body = response.json()
            validate(response_json_body, post_favorites)

    @allure.title('Получение списка избранных фильмов')
    def test_get_favorite(self, auth, endpoint_url):
        response = api.get_favorites(auth, endpoint_url)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

        with allure.step('Валидация JSON-схемы'):
            response_json_body = response.json()
            validate(response_json_body, get_favorites)

    @allure.title('Удаление из избранных фильма')
    def test_delete_favorite(self, auth, endpoint_url):
        film_id = cfg.film_id
        response_add_to_favorite = api.add_to_favorite(auth, endpoint_url, film_id)
        response = api.delete_favorite_film(auth, endpoint_url, film_id)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

