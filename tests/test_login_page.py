import pytest
from pages.login_page import LoginPage
from tests.conftest import login_page

def test_login_success(login_page):

    expected = "Congratulations! You must have the proper credentials."
    actual = LoginPage.success_message.inner_text()
    
    assert actual == expected, f"Expected text: '{expected}', but got: '{actual}'"
