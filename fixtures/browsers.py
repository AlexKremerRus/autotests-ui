import pytest
from playwright.sync_api import  expect, Page, Playwright
from pages.aurhentification.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
import allure

@pytest.fixture
def chromium_page(request:SubRequest, playwright: Playwright) -> Page:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context.new_page()
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username="username", password="password")
    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(request:SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')

    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')







