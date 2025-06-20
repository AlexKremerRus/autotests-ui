import pytest

from tools.allure.environment import create_allure_env_file


@pytest.fixture(scope='session', autouse=True)
def save_allure_env_file():
    yield
    create_allure_env_file()