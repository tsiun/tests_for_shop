from pages.base_page import BasePage
from playwright.sync_api import Page
from ui.web_element import WebElement


class UploadImagePage(BasePage):
    def __init__(self, page: Page, config: dict):
        super().__init__(page, config)
        self.image_upload = WebElement(
            self.page.locator("#file-upload"),
            description="Upload page -> file upload"
        )
        self.submit_button = WebElement(
            self.page.get_by_role('button', name='Upload'),
            description="Uploaded file -> submit button"
        )
        self.check_file_name = WebElement(
            self.page.locator("#uploaded-files"),
            description="Uploaded file -> check file_name"
        )

    def upload_file(self, file_path: str) -> None:
        self.image_upload.set_input_files(file_path=file_path)

        self.submit_button.click()

    def check_result(self) -> str:
        return self.check_file_name.get_inner_text()
