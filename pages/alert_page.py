from playwright.sync_api import Page
from ui.web_element import WebElement
from logger import setup_logger
from pages.base_page import BasePage
from ui.page_actions import PageActions

logger = setup_logger(__name__)

class AlertPage(BasePage):
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.page_actions = PageActions(page)
        self.trigger_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Alert"),
            description="Alert page -> Alert show"
        )

    def trigger_alert_and_accept(self) -> str:
        return self.page_actions.run_and_accept_alert(self.trigger_button.click)

