from playwright.sync_api import Page
from ui.web_element import WebElement
from ui.base_page import BasePage

class LoginPage(BasePage):
    _path = "/basic_auth"
    _requires_basic_auth = True
    
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.success_message = WebElement(
            locator = self.page.get_by_test_id('content').locator('p'),
            description="Auth page -> endpoint page",
        )
