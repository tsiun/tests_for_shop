from playwright.sync_api import Page
from ui.web_element import WebElement

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.success_message = WebElement(
            self.page.get_by_test_id('content'),
            description="Auth page -> endpoint page",
        )