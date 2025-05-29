import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)