from pages.hovers_page import HoversPage


def test_hovers(hovers_page: HoversPage) -> None:
    users = hovers_page.get_list_of_users()

    for index, actual_list in enumerate(users, start=1):
        expected_list = f"name: user{index}"

    assert actual_list == expected_list, f"Expected users: {expected_list}, but got: {actual_list}"
