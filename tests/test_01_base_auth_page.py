from pages.base_auth_page import BaseAuth

def test_base_auth_success(base_auth_page: BaseAuth) -> None:

    actual = "Congratulations! You must have the proper credentials."
    expected = base_auth_page.get_success_message()

    assert actual == expected, f"Expected text: '{expected}', but got: '{actual}'"