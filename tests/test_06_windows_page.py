from pages.windows_page import WindowsPage


def test_windows(windows_page: WindowsPage):
    main_wind_page = windows_page.page

    second_wind_page = windows_page.make_click()

    actual_step_one = second_wind_page.get_text()
    expected_step_one = "New Window"

    assert actual_step_one == expected_step_one, f"Expected text: {expected_step_one}, but got: {actual_step_one}"

    main_wind_page.bring_to_front()

    second_wind_page_obj_two = windows_page.make_click()

    actual_step_two = second_wind_page_obj_two.get_text()
    expected_step_two = "New Window"

    assert actual_step_two == expected_step_two, f"Expected text: {expected_step_two}, but got: {actual_step_two}"

    main_wind_page.bring_to_front()

    second_wind_page.page.close()
    second_wind_page_obj_two.page.close()

    actual_step_three = len(main_wind_page.context.pages)
    expected_step_three = 1

    assert actual_step_three == expected_step_three, f"Expected text: {expected_step_three}, but got: {actual_step_three}"
