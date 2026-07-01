from playwright.sync_api import Page
from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.user_avatars = MultiWebElement(
            page=self.page,
            locator=self.page.get_by_alt_text("User Avatar"),
            description="Hover Page -> point to image"
        )
        self.user_names = MultiWebElement(
            page=self.page,
            locator=self.page.get_by_text("name: user", exact=False),
            description="Hover Page -> user name"
        )

    def get_list_of_users(self) -> list[str]:
        result = []
        count = self.user_avatars.count()

        for i in range(count):
            self.user_avatars.nth(i).hover()
            popup_text = self.user_names.nth(i).get_inner_text()
            result.append(popup_text)

        return result
