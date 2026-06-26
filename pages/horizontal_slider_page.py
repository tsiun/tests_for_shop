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

    
    def _calc_random_steps(self, min_val=0.0, max_val=5.0, step=0.5):
        total_steps = round((max_val - min_val) / step)
        n_steps = randint(1, total_steps - 1)
        value_of_slider = round(min_val + n_steps * step, 10)

        return value_of_slider, n_steps
    

    def move_slider_randomly(self, min_val=0.0, max_val=5.0, step=0.5) -> float:
        expected_value, steps = self._calc_random_steps(min_val, max_val, step)
        
        self.slider.focus()
        for _ in range(steps):
            self.slider.locator.press("ArrowRight")


        return expected_value


    def get_result_value(self) -> float:
        return float(self.result_value.get_inner_text())