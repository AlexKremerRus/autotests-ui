from components.base_component import BaseComponent
from  playwright.sync_api import Page, expect
import re
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
import allure

class SidebarComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

        self.dashboard_list_item=SidebarListItemComponent(page, identifier='dashboard')
        self.courses_list_item=SidebarListItemComponent(page, identifier='courses')
        self.logout_list_item=SidebarListItemComponent(page, identifier='logout')


    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.dashboard_list_item.check_visible(title='Dashboard')
        self.courses_list_item.check_visible(title='Courses')
        self.logout_list_item.check_visible(title='Logout')

    @allure.step("Click logout on sidebar")
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))

    @allure.step("Click courses on sidebar")
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))