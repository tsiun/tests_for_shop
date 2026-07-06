from pages.nested_frames_page import NestedFramesPage


def test_nested_frames(nested_frames_page: NestedFramesPage):
    actual_left = nested_frames_page.get_left_text()
    expected_left = "LEFT"

    assert actual_left == expected_left, f"Expected text: {expected_left}, but got: {actual_left}"

    actual_right = nested_frames_page.get_right_text()
    expected_right = "RIGHT"

    assert actual_right == expected_right, f"Expected text: {expected_right}, but got: {actual_right}"

    actual_bottom = nested_frames_page.get_bottom_text()
    expected_bottom = "BOTTOM"

    assert actual_bottom == expected_bottom, f"Expected text: {expected_bottom}, but got: {actual_bottom}"

    actual_middle = nested_frames_page.get_middle_text()
    expected_middle = "MIDDLE"

    assert actual_middle == expected_middle, f"Expected text: {expected_middle}, but got: {actual_middle}"
