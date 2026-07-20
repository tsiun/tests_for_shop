from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.web_element import WebElement


class WindowsSecondPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.main_text = WebElement(
            locator=self.page.get_by_role("heading", name="New Window"),
            description="Second windows page -> get text"
        )

    def get_text(self) -> str:
        return self.main_text.get_inner_text()
