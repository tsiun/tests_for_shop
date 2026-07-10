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
            description="Scroll page -> dynamic paragraphs"
        )

    def get_paragraphs_count(self) -> int:
        return self.dynamic_paragraphs.count()

    def scroll_down_by_paragraphs(self, count: int) -> None:
        for i in range(count):
            self.page.mouse.wheel(delta_x=0, delta_y=10000)

            current_paragraph = self.dynamic_paragraphs.nth(i)

            current_paragraph.scroll_into_view_if_needed()

            current_paragraph.wait_for(state='visible', timeout=5000)
