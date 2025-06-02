from playwright.sync_api import Page, expect
from typing import Pattern

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, external_url: Pattern[str]):
        expect(self.page).to_have_url(external_url)