from utils.url_utils import embed_credentials_in_url
from logger import get_logger
from ui.page_factory import PageFactory

logger = get_logger(__name__)


class BasePage(PageFactory):
    _path: str = ""
    _requires_basic_auth: bool = False

    def __init__(self, page, config: dict) -> None:
        self.page = page
        self.config = config
        self._init_elements()

    def open(self) -> None:
        base_url = self.config["base_url"]
        url = f"{base_url}{self._path}"

        if self._requires_basic_auth:
            auth = self.config["basic_auth"]
            url = embed_credentials_in_url(url, auth["username"], auth["password"])

        logger.info(f"Opening: {url}")
        self.page.goto(url)
