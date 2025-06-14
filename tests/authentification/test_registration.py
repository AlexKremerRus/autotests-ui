import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature
from allure_commons.types import Severity


from pages.dashboard.dashboard_page import DashboardPage
from pages.aurhentification.registration_page import RegistrationPage

@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION )
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.story(AllureStories.REGISTRATION)
@allure.severity(Severity.BLOCKER)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTIFICATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    def test_successful_registration(self,registration_page: RegistrationPage, dashboard_page:DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()
