from playwright.sync_api import Page
from ui.web_element import WebElement
from logger import setup_logger
from pages.base_page import BasePage

logger = setup_logger(__name__)

class AlertPage(BasePage):
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.trigger_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Alert"),
            description="Alert page -> Alert show"
        )

    def trigger_alert_and_accept(self) -> str:
        with self.page.expect_event("dialog") as dialog_info:
            self.trigger_button.click()

        dialog = dialog_info.value
        message = dialog.message

        logger.info(f"Перехвачен алерт с текстом: {dialog.message}")

        dialog.accept()

        return message


