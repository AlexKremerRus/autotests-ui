import pytest
from pages.aurhentification.login_page import LoginPage
from pages.aurhentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag( AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.story(AllureStories.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTIFICATION)
@allure.sub_suite(AllureStories.AUTHORIZATION)
class TestAuthorization:
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.title("User login with correct email and password")
    def test_successful_authorization(self, registration_page:RegistrationPage, dashboard_page: DashboardPage, login_page:LoginPage ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email='test@test.test', username='AlexMan', password="Passw0rd")
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible('AlexMan')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='test@test.test', password="Passw0rd")
        login_page.click_login_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible('AlexMan')
        dashboard_page.sidebar.check_visible()


    @pytest.mark.parametrize('email, password',
                             [("user.name@gmail.com", "password"),
                              ("user.name@gmail.com", "  "),
                              ("  ", "password")
                              ])

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self,login_page: LoginPage, email: str, password: str):

        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self, login_page:LoginPage, registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")

