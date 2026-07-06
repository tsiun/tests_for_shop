from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.web_element import WebElement


class NestedFramesPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.left_frame = WebElement(
            self.page.frame_locator(
                "frame[name='frame-top']").frame_locator("frame[name='frame-left']").get_by_text("LEFT"),
            description="Frames page -> Left frame",
        )
        self.right_frame = WebElement(
            self.page.frame_locator(
                "frame[name='frame-top']").frame_locator("frame[name='frame-right']").get_by_text("RIGHT"),
            description="Frames page -> Right frame",
        )
        self.bottom_frame = WebElement(
            self.page.frame_locator(
                "frame[name='frame-bottom']").get_by_text("BOTTOM"),
            description="Frames page -> Bottom frame",
        )
        self.middle_frame = WebElement(
            self.page.frame_locator(
                "frame[name='frame-top']").frame_locator("frame[name='frame-middle']").get_by_text("MIDDLE"),
            description="Frames page -> Middle frame",
        )

    def get_left_text(self) -> str:
        return self.left_frame.get_inner_text()

    def get_right_text(self) -> str:
        return self.right_frame.get_inner_text()

    def get_bottom_text(self) -> str:
        return self.bottom_frame.get_inner_text()

    def get_middle_text(self) -> str:
        return self.middle_frame.get_inner_text()
