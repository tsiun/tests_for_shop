from playwright.sync_api import Page, expect
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
    
    page.get_by_role('button', name='Confirm').click()
    expect(page.get_by_text('Invalid login or password.')).to_be_visible()