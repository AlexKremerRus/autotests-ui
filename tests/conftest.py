import pytest
from playwright.sync_api import sync_playwright, expect, Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.firefox.launch(headless=False)
    yield browser.new_page()