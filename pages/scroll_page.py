from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.page_actions = PageActions(page)
        self.dynamic_paragraphs = MultiWebElement(
            page=self.page,
            locator=self.page.locator("#content .jscroll-added"),
            description="Scroll page -> dynamic paragraphs",
        )

    def get_paragraphs_count(self) -> int:
        return self.dynamic_paragraphs.count()

    def scroll_down_by_paragraphs(self, count: int) -> None:
        while self.get_paragraphs_count() < count:
            current_count = self.get_paragraphs_count()
            current_paragraph = self.dynamic_paragraphs.last()

            current_paragraph.scroll_into_view_if_needed()

            self.dynamic_paragraphs.nth(current_count).is_visible()
