from pages.horizontal_slider_page import HorizontalSliderPage
from utils.slider_utils import get_random_slider_value


def test_horizontal_slider(horizontal_slider_page: HorizontalSliderPage) -> None:
    min_val = horizontal_slider_page.get_min_val()
    max_val = horizontal_slider_page.get_max_val()
    step = horizontal_slider_page.get_step()

    expected_value = get_random_slider_value(min_val, max_val, step)
    horizontal_slider_page.move_slider_to_value(target_value=expected_value)
    actual_value = horizontal_slider_page.get_current_value()

    assert actual_value == expected_value, f"Expected value: '{expected_value}', but got: '{actual_value}'"
