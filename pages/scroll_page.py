from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.multi_web_element import MultiWebElement


class ScrollPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.dynamic_paragraphs = MultiWebElement(
            page=self.page,
            locator=self.page.locator("#content .jscroll-added"),
            description="Scroll page -> dynamic paragraphs"
        )

    def scroll_down_by_paragraphs(self, count: int = 10) -> None:
        for i in range(count):
            current_paragraph = self.dynamic_paragraphs.nth(i)

            current_paragraph.scroll_into_view_if_needed()

            self.page.wait_for_timeout(500)

    def get_paragraphs_count(self) -> int:
        return self.dynamic_paragraphs.count()
