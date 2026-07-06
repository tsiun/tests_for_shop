from pages.context_menu_page import ContextMenuPage


def test_context_menu(context_menu_page: ContextMenuPage) -> None:
    actual_context = context_menu_page.make_right_click()
    expected_context = 'You selected a context menu'

    assert actual_context == expected_context, f"Expected text: '{expected_context}', but got: '{actual_context}'"
