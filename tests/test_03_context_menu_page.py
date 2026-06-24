import pytest
from pages.context_menu_page import ContextMenu

def test_context_menu(context_menu_page: ContextMenu) -> None:
    actual_context = context_menu_page.make_right_click()
    expected_context = 'You selected a context menu'
    
    assert actual_context == expected_context, f"Expected text: '{expected_context}', but got: '{actual_context}'"