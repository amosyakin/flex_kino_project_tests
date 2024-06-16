import os

import pytest
from dotenv import load_dotenv

from flex_kino_project_tests.model.api import api
from flex_kino_project_tests.utils import attach


load_dotenv()

user_email = os.getenv('USER_EMAIL')
user_password = os.getenv('USER_PASSWORD')
domain_url = os.getenv('DOMAIN_URL')
api_v = os.getenv('API_V')
film_id = os.getenv('FILM_ID')


@pytest.fixture(scope="function")
def auth(endpoint_url):
    response = api.login(endpoint_url)
    return response


@pytest.fixture(scope='function')
def endpoint_url():
    base_url = domain_url + api_v
    return base_url


@pytest.fixture(scope="function")
def add_attach(response):
    yield response

    attach.add_api_attach(response)
