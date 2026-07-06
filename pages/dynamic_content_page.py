from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from playwright.sync_api import Page


class DynamicContentPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.dynamic_images = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".large-2.columns img"),
            description="Dynamic page -> dynamic images"
        )

    def get_image_sources(self) -> list[str]:
        return [img.get_attribute("src") for img in self.dynamic_images.all()]

    def has_duplicate_img_src(self) -> bool:
        img_sourses = self.get_image_sources()
        return len(set(img_sourses)) < len(img_sourses)

    def wait_for_duplicate_images(self, max_attempts: int = 3) -> bool:
        for attempt in range(1, max_attempts + 1):
            if self.has_duplicate_img_src():
                return True

            self.page.reload()

            # self.dynamic_image.wait_for(state="visible")
            # self.page.wait_for_timeout(timeout=5000)
            # self.dynamic_image.first().wait_for(state="visible")
            # self.dynamic_image.wait_for_load_state()
            self.page.wait_for_load_state("load")

        return False
