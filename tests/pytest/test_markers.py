import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_case_1(self):
        ...

    def test_case_2(self):
        pass


@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass