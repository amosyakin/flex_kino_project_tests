import pytest

import cfg

from qa_guru_diplom.model.api import api
from utils import attach


@pytest.fixture(scope="function")
def auth(endpoint_url):
    response = api.login(endpoint_url)
    return response


@pytest.fixture(scope='function')
def endpoint_url():
    base_url = cfg.domain_url + cfg.api_v
    return base_url


@pytest.fixture(scope="function")
def add_attach(response):
    yield response

    attach.add_api_attach(response)
