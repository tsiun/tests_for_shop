from playwright.sync_api import Page, expect
from config import BASE_URL

def test_login(page: Page):
    page.goto(BASE_URL)
    page.get_by_test_id('nav-login').click()
    page.get_by_test_id('login-username').fill('testDataLogin')
    page.get_by_test_id('login-password').fill('testDataPassword')
    page.get_by_role('button', name='Confirm').click()
    expect(page.get_by_text('Invalid login or password.')).to_be_visible()