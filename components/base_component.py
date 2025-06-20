from playwright.sync_api import Page, expect
from typing import Pattern
import allure

from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, external_url: Pattern[str]):
        step = f"Check current url {external_url}"
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(external_url)