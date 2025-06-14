# /pages/base_page.py
import allure
from playwright.sync_api import Page, expect
from typing import Pattern

class BasePage:
    def __init__(self, page: Page):
        self.page = page


    def visit(self, url: str):
        with allure.step(f'Opening url {url}'):
            self.page.goto(url, wait_until='networkidle')  # у меня сомнения на то что нужно дожидаться всех нетворков

    def reload(self):
        with allure.step(f'Reload url {self.page.url}'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, external_url: Pattern[str]):
        with allure.step(f'Checking that current  url {external_url.pattern}'):
            expect(self.page).to_have_url(external_url)

