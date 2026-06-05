import pytest
from pages.login_page import LoginPage
from tests.conftest import auth_page

def test_login(auth_page):
    login_page = LoginPage(auth_page)
    login_page.open(auth_page.url)

    expected = "Congratulations! You must have the proper credentials."
    actual = login_page.get_text_content()
    
    assert actual == expected, f"Expected text: '{expected}', but got: '{actual}'"
