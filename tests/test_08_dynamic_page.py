from pages.dynamic_content_page import DynamicContent


def test_dynamic_content(dynamic_content_page: DynamicContent):
    max_attempts = 4

    actual = dynamic_content_page.get_duplicate_imgs(max_attempts=max_attempts)
    expected = True

    assert actual == expected, f"Expected result: 'two identical images were found on the page', but got: 'After {max_attempts} attempts of refresh the page, there are no identical images on the page'"
