import pytest
from pages.login_page import LoginPage
from pages.login_endpoint_page import EndpointPage

def test_login_success(endpoint_page: EndpointPage) -> None:

    expected = "Congratulations! You must have the proper credentials."
    actual = endpoint_page.get_success_message()

    assert actual == expected, f"Expected text: '{expected}', but got: '{actual}'"