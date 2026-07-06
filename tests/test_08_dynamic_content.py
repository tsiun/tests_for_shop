from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content(dynamic_content_page: DynamicContentPage):
    max_attempts = 4

    actual = dynamic_content_page.wait_for_duplicate_images(
        max_attempts=max_attempts)
    expected = True

    assert actual == expected, (
        f"Expected result: 'two identical images were found on the page', "
        f"but got: 'After {max_attempts} attempts of refreshing the page, "
        f"there are no identical images on the page'"
    )
