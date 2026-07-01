from pages.alert_page import AlertPage
from pages.alert_page import random_word


def test_alert_text(alert_page: AlertPage) -> None:

    actual_alert = alert_page.click_alert_and_accept()
    expected_alert = 'I am a JS Alert'
    assert actual_alert == expected_alert, f"Expected text: '{expected_alert}', but got: '{actual_alert}'"

    result_alert = alert_page.get_result_text()
    expected_result_alert = 'You successfully clicked an alert'
    assert result_alert == expected_result_alert, f"Expected text: '{expected_result_alert}', but got: '{result_alert}'"

    actual_confirm = alert_page.click_confirm_and_accept()
    expected_confirm = 'I am a JS Confirm'
    assert actual_confirm == expected_confirm, f"Expected text: '{expected_confirm}', but got: '{actual_confirm}'"

    result_confirm = alert_page.get_result_text()
    expected_result_confirm = 'You clicked: Ok'
    assert result_confirm == expected_result_confirm, f"Expected text: '{expected_result_confirm}', but got: '{result_confirm}'"

    actual_prompt = alert_page.click_prompt_and_input()
    expected_prompt = 'I am a JS prompt'
    assert actual_prompt == expected_prompt, f"Expected text: '{expected_prompt}', but got: '{actual_prompt}'"

    result_prompt = alert_page.get_result_text()
    expected_result_prompt = f'You entered: {random_word}'
    assert result_prompt == expected_result_prompt, f"Expected text: '{expected_result_prompt}', but got: '{result_prompt}'"
