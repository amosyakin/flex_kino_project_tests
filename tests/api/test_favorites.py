import allure
from allure_commons.types import Severity
from jsonschema import validate

from flex_kino_project_tests.model.api import api
from flex_kino_project_tests.schemas.favorites import post_favorites, get_favorites
from tests.api import conftest


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.epic('API')
@allure.feature('Favorites')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1259')
class TestFavorites:
    @allure.id("32834")
    @allure.title('Добавление в избранное фильма')
    def test_add_favorite(self, auth, endpoint_url):
        film_id = int(conftest.film_id)
        response = api.add_to_favorite(auth, endpoint_url, film_id)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 201

        with allure.step('Проверка ответа Response'):
            response_json = response.json()
            assert response_json['id'] == film_id

        with allure.step('Валидация JSON-схемы'):
            response_json_body = response.json()
            validate(response_json_body, post_favorites)

    @allure.id("32835")
    @allure.title('Получение списка избранных фильмов')
    def test_get_favorite(self, auth, endpoint_url):
        film_id = int(conftest.film_id)
        api.add_to_favorite(auth, endpoint_url, film_id)
        response = api.get_favorites(auth, endpoint_url)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

        with allure.step('Проверка ответа Response'):
            response_json = response.json()
            assert response_json['results'][0]['id'] == film_id

        with allure.step('Валидация JSON-схемы'):
            response_json_body = response.json()
            validate(response_json_body, get_favorites)

    @allure.id("32836")
    @allure.title('Удаление из избранных фильма')
    def test_delete_favorite(self, auth, endpoint_url):
        film_id = int(conftest.film_id)
        api.add_to_favorite(auth, endpoint_url, film_id)
        response = api.delete_favorite_film(auth, endpoint_url, film_id)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

        with allure.step('Проверка ответа Response'):
            assert response.text == ''
