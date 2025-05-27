import pytest
from playwright.sync_api import sync_playwright, expect, Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.firefox.launch(headless=False)
    yield browser.new_page()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()

    context.storage_state(path='browser-state.json')

    browser.close()



@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()






