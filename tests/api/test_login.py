import allure
from allure_commons.types import Severity
from jsonschema.validators import validate

from qa_guru_diplom.model.api import api
from qa_guru_diplom.schemas.login import post_login


@allure.id("32837")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1259')
@allure.epic('API')
@allure.feature('Authorization')
@allure.title('Авторизация пользователя')
def test_login(endpoint_url):
    response = api.login(endpoint_url)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    with allure.step('Валидация JSON-схемы'):
        response_json_body = response.json()
        validate(response_json_body, post_login)
