from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.multi_web_element import MultiWebElement
from pathlib import Path


class DownloadPage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.file_names = MultiWebElement(
            page=self.page,
            locator=self.page.locator(".example a"),
            description="Download page -> safe exact file"
        )

    def get_exact_file_name(self, position: int = 3) -> str:
        exact_file = self.file_names.nth(position - 1)
        file_name = exact_file.get_inner_text()
        return file_name

    def download_exact_file(self) -> str:
        file_name = self.get_exact_file_name()

        with self.page.expect_download() as download_info:
            self.page.get_by_text(file_name).click()

        download = download_info.value
        save_path = Path("downloads") / download.suggested_filename
        download.save_as(save_path)

        return save_path
