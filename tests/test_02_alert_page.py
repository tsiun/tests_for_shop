from pages.alert_page import AlertPage
from pages.alert_page import random_word

def test_alert_text(alert_page: AlertPage) -> None:

    expected_alert = alert_page.click_alert_and_accept()
    actual_alert = 'I am a JS Alert'
    assert actual_alert == expected_alert, f"Expected text: '{expected_alert}', but got: '{actual_alert}'"

    expected_result_alert = alert_page.get_result_text()
    result_alert = 'You successfully clicked an alert'
    assert result_alert == expected_result_alert, f"Expected text: '{expected_result_alert}', but got: '{result_alert}'"

    expected_confirm = alert_page.click_confirm_and_accept()
    actual_confirm = 'I am a JS Confirm'
    assert actual_confirm == expected_confirm, f"Expected text: '{expected_confirm}', but got: '{actual_confirm}'"

    expected_result_confirm = alert_page.get_result_text()
    result_confirm = 'You clicked: Ok'
    assert result_confirm == expected_result_confirm, f"Expected text: '{expected_result_confirm}', but got: '{result_confirm}'"

    expected_prompt = alert_page.click_prompt_and_input()
    actual_prompt = 'I am a JS prompt'
    assert actual_prompt == expected_prompt, f"Expected text: '{expected_prompt}', but got: '{actual_prompt}'"

    expected_result_prompt = alert_page.get_result_text()
    result_prompt = f'You entered: {random_word}'
    assert result_prompt == expected_result_prompt, f"Expected text: '{expected_result_prompt}', but got: '{result_prompt}'"

