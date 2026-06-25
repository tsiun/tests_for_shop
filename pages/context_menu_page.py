from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.web_element import WebElement
from logger import setup_logger
from ui.page_actions import PageActions

logger = setup_logger(__name__)

class ContextMenu(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.page_actions = PageActions(page)
        self.hot_spot_area = WebElement(
            self.page.locator("#hot-spot"),
            description="Context menu page -> Hot spot area"
        )
        


    def make_right_click(self) -> str:
        
        return self.page_actions.run_and_accept_alert(self.hot_spot_area.right_click)