# /pages/base_page.py
import allure
from playwright.sync_api import Page, expect
from typing import Pattern
from tools.logger import get_logger


logger = get_logger("BASE_PAGE")

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Opening url {url}'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')  # у меня сомнения на то что нужно дожидаться всех нетворков

    def reload(self):
        step = f'Reload url {self.page.url}'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, external_url: Pattern[str]):
        step = f'Checking that current  url {external_url.pattern}'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(external_url)

