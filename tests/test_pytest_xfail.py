import pytest

# опсле запуска tests/test_pytest_xfail.py::test_with_bug XFAIL
@pytest.mark.xfail
def test_with_bug():
    assert 1==2

# после запуска tests/test_pytest_xfail.py::test_without_bug XPASS
@pytest.mark.xfail
def test_without_bug():
    ...