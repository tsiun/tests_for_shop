from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from playwright.sync_api import Page


class DynamicContent(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.dynamic_image = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".large-2.columns img"),
            description="Dynamic page -> dynamic images"
        )

    def get_count_img_src(self) -> list[str]:
        count_imgs = len(self.dynamic_image.all())
        sourses = []

        for i in range(count_imgs):
            example = self.dynamic_image.get_attribute("src")
            sourses.append(example)

        return sourses

    def has_duplicate_img_src(self) -> bool:
        check_duplicate = self.get_count_img_src()
        return len(set(check_duplicate)) < len(check_duplicate)

    def get_duplicate_imgs(self, max_attempts: int = 3) -> bool:
        for attempt in range(1, max_attempts + 1):
            if self.has_duplicate_img_src:
                print(f"Дубликаты найдены на попытке {attempt}")
                return True

            self.page.reload()

            # self.dynamic_image.wait_for(state="visible")
            # self.page.wait_for_timeout(timeout=5000)
            self.dynamic_image.first.wait_for(state="visible")

        print(f"После {attempt} попыток дубликаты не найдены.")
        return False
