from components.base_component import BaseComponent
from  playwright.sync_api import Page, expect
import re
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

        self.dashboard_list_item=SidebarListItemComponent(page, identifier='dashboard')
        self.courses_list_item=SidebarListItemComponent(page, identifier='courses')
        self.logout_list_item=SidebarListItemComponent(page, identifier='logout')

    def check_visible(self):
        self.dashboard_list_item.check_visible(title='Dashboard')
        self.courses_list_item.check_visible(title='Courses')
        self.logout_list_item.check_visible(title='Logout')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))