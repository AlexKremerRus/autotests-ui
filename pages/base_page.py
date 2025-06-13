# /pages/base_page.py

from playwright.sync_api import Page, expect
from typing import Pattern

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')  # у меня сомнения на то что нужно дожидаться всех нетворков

    def reload(self):
        self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, external_url: Pattern[str]):
        expect(self.page).to_have_url(external_url)

