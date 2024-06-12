import allure
from allure_commons.types import Severity
from jsonschema.validators import validate

from qa_guru_diplom.schemas.site_info import get_site_info
from qa_guru_diplom.model.api import api


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1259')
@allure.epic('API')
@allure.feature('Site info')
@allure.title('Список приложений')
@allure.id("32838")
def test_site_info(endpoint_url):
    response = api.get_site_info(endpoint_url)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    with allure.step('Валидация JSON-схемы'):
        response_json_body = response.json()
        validate(response_json_body, get_site_info)
