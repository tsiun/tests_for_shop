import pytest
from pages.alert_page import AlertPage

def test_alert_text(alert_page: AlertPage) -> None:

    actual_message = alert_page.trigger_alert_and_accept()
    expected_message = 'I am a JS Alert'

    assert actual_message == expected_message, f"Expected text: '{expected_message}', but got: '{actual_message}'"