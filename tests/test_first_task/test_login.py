from playwright.sync_api import Page
from config import BASE_URL
from faker import Faker

fake = Faker()

def test_login(page: Page):
    page.goto(BASE_URL)
    page.get_by_test_id('nav-login').click()

    username = fake.user_name()
    password = fake.password()

    page.get_by_test_id('login-username').fill(username)
    page.get_by_test_id('login-password').fill(password)

    page.get_by_test_id('login-submit').click()

    loader = page.get_by_test_id('login-submit-spinner')

    loader.wait_for(state='visible')
    loader.wait_for(state='hidden')

    expected_error = "Invalid login or password."
    actual_error = page.get_by_test_id('login-error-inline').inner_text()

    assert actual_error == expected_error, \
    f"Expected '{expected_error}', but got '{actual_error}'"
