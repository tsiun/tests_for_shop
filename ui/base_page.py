from playwright.sync_api import Page
from utils.url_utils import embed_credentials_in_url
from logger import setup_logger
from urllib.parse import urljoin

logger = setup_logger(__name__)


class BasePage:
    _path: str = ""
    _requires_basic_auth: bool = False

    def __init__(self, page: Page, config: dict) -> None:
        self.page = page
        self.config = config

    def open(self) -> None:
        base_url = self.config["base_url"]
        url = urljoin(base_url, self._path)

        if self._requires_basic_auth:
            auth = self.config["basic_auth"]
            url = embed_credentials_in_url(url, auth["username"], auth["password"])

        logger.info(f"Opening: {url}")
        self.page.goto(url)
