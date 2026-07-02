from pages.base_page import BasePage
from ui.web_element import WebElement
from playwright.sync_api import Page
from pages.windows_second_page import WindowsSecondPage


class WindowsPage(BasePage):
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.main_link = WebElement(
            locator=self.page.get_by_role("link", name="Click Here"),
            description="Windows Page -> Click to link"
        )

    def make_click(self) -> WindowsSecondPage:
        with self.page.context.expect_page() as new_page_catch:
            self.main_link.click()
        new_tab = new_page_catch.value

        return WindowsSecondPage(page=new_tab, config=self.config)
