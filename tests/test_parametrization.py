from math import lgamma

import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1,2,3,-1])
def test_number(number:int):
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1,1),(2,4),(3,9),(4,16)])
def test_several_numbers(number: int, expected: int):
    assert number**2 == expected

@pytest.mark.parametrize('os', ['macos', 'windows', 'linux'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os : str, browser: str):
    print(f"{os} - {browser}")


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(browser)

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperation:
    @pytest.mark.parametrize('account', ['credit', 'debit'])
    def test_user_with_operation(self, user:str, account: str):
        pass

    def test_user_without_operation(self, user: str):
        pass

users = {
    '79001232001':'with money',
    '79001232002':'without money',
    '79001232003':'with operation'
}

@pytest.mark.parametrize('phone_number', users.keys(), ids=lambda phone_number: f"{phone_number} : {users[phone_number]}")
def test_identifiers(phone_number: str):
    pass