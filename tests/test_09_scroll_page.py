from pages.scroll_page import ScrollPage


def test_scroll_page(scroll_page: ScrollPage):
    expected = 10

    scroll_page.scroll_down_by_paragraphs(count=expected)
    actual = scroll_page.get_paragraphs_count()

    assert actual >= expected, (
        f"Expected more than or equal to {expected} paragraphs on the page', "
        f"but got: '{actual}'"
    )
