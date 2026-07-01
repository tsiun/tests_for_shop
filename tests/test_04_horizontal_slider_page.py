from pages.horizontal_slider_page import HorizontalSlider


def test_horizontal_slider(horizontal_slider_page: HorizontalSlider) -> None:
    actual_value = horizontal_slider_page.move_slider_randomly()
    expected_value = horizontal_slider_page.get_result_value()

    assert actual_value == expected_value, f"Expected text: '{expected_value}', but got: '{actual_value}'"
