from playwright.sync_api import Page
from ui.base_page import BasePage
from ui.web_element import WebElement

class EndpointPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.success_message = WebElement(
            locator=self.page.get_by_text("Congratulations! You must have the proper credentials."),
            description="Popup page -> success message after auth"
        )

    def get_success_message(self) -> str:
        return self.success_message.get_text_content().strip()
    
    def is_success_message_visible(self) -> bool:
        return self.success_message.locator.is_visible()