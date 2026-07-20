from playwright.sync_api import Page
from logger import setup_logger

logger = setup_logger(__name__)

class BasePage:

    def __init__(self, page: Page, config: dict) -> None:
        self.page = page
        self.config = config

