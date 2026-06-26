from pages.login_endpoint_page import EndpointPage

def test_login_success(endpoint_page: EndpointPage) -> None:

    actual = "Congratulations! You must have the proper credentials."
    expected = endpoint_page.get_success_message()

    assert actual == expected, f"Expected text: '{expected}', but got: '{actual}'"