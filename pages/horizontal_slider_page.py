from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.web_element import WebElement
from random import randint


class HorizontalSlider(BasePage):
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.slider = WebElement(
            self.page.get_by_role("slider"),
            description="Horizontal slider page -> Move Slider"
        )
        self.result_value = WebElement(
            self.page.locator("#range"),
            description="Horizontal slider page -> Slider value"
        )

    def get_min_val(self) -> float:
        return float(self.slider.get_attribute("min"))

    def get_max_val(self) -> float:
        return float(self.slider.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.slider.get_attribute("step"))

    def get_current_value(self) -> float:
        return float(self.result_value.get_inner_text())

    def move_slider_to_value(self, target_value: float) -> None:
        min_val = self.get_min_val()
        # max_val = self.get_max_val()
        step = self.get_step()

        steps_count = round((target_value - min_val) / step)

        self.slider.focus()
        for _ in range(steps_count):
            self.slider.locator.press("ArrowRight")
