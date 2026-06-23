from playwright.sync_api import Page
from ui.web_element import WebElement
from logger import setup_logger
from pages.base_page import BasePage
from ui.page_actions import PageActions
from faker import Faker

logger = setup_logger(__name__)

fake = Faker()
random_word = fake.word()

class AlertPage(BasePage):
    def __init__(self, page: Page, config: dict) -> None:
        super().__init__(page, config)
        self.page_actions = PageActions(page)
        self.alert_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Alert"),
            description="Alert page -> Alert button"
        )
        self.confirm_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Confirm"),
            description="Alert page -> Confirm button"
        )
        self.prompt_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Prompt"),
            description="Alert page -> Prompt button"
        )
        self.result_text = WebElement(
            self.page.locator("#result"),
            description="Alert page -> text inside result block"
        )

    def click_alert_and_accept(self) -> str:
        return self.page_actions.run_and_accept_alert(self.alert_button.click)
    
    def click_confirm_and_accept(self) -> str:
        return self.page_actions.run_and_accept_alert(self.confirm_button.click)
    
    def click_prompt_and_input(self) -> str:
        return self.page_actions.run_and_accept_prompt(self.prompt_button.click, prompt_text=f"{random_word}")
    
    def get_result_text(self) -> str:
        return self.result_text.get_text_content()