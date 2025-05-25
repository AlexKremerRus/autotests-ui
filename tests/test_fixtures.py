import pytest

@pytest.fixture(autouse=True)  # Автоматический запуск перед тестами - запускается без передачи - на каждый тест
def send_analytics():
    print("send")

@pytest.fixture(scope='session') # запускается один раз на сессию (на запуск всех тестов один раз )
def settings_session():
    print('settings_session')

@pytest.fixture(scope='class') # запускается один раз на тестовый класс (каждый класс - каждый запуск фикстуры)
def settings_class():
    print('settings_class')

@pytest.fixture(scope='function') # запускается один раз на тестовый функцию (каждый класс - каждый запуск фикстуры)
def settings_function():
    print('settings_function')


class TestUserFlow:
    def test_user_can_login(self, settings_session, settings_class, settings_function):
        pass

    def test_user_can_create_user(self, settings_session, settings_class, settings_function):
        pass

class TestAccountFlow:
    def test_user_flow(self, settings_session, settings_class, settings_function):
        pass

# для запуска  python -m pytest -s -v -k "TestUserFlow or TestAccountFlow"