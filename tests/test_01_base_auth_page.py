from pages.base_auth_page import BaseAuthPage


def test_base_auth_success(base_auth_page: BaseAuthPage) -> None:

    expected = "Congratulations! You must have the proper credentials."
    actual = base_auth_page.get_success_message()

    assert actual == expected, f"Expected text: '{expected}', but got: '{actual}'"
