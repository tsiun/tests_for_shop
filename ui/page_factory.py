import json
from logger import setup_logger
from urllib.parse import urljoin
from utils.url_utils import embed_credentials_in_url
from ui.page_actions import PageActions

from playwright.sync_api import Browser, BrowserContext, Page

logger = setup_logger(__name__)

class PageFactory:
    DEFAULT_USER_AGENT = "Steam3TestRunner/1.0"
    DEFAULT_VIEWPORT = {"width": 1440, "height": 900}
    DEFAULT_LOCALE = "en-US"
    DEFAULT_TIMEZONE_ID = "Europe/Moscow"
    DEFAULT_COLOR_SCHEME = "light"
    DEFAULT_IGNORE_HTTPS_ERRORS = True
    DEFAULT_TIMEOUT_MS = 10_000
    DEFAULT_NAVIGATION_TIMEOUT_MS = 15_000
    DEFAULT_ENABLE_TRACING = True
    DEFAULT_BLOCK_ANALYTICS = True

    def __init__(self, browser: Browser, config: dict) -> None:
        self.browser = browser
        self.config = config

    @classmethod
    def from_json(cls, browser: Browser, file_path: str) -> PageFactory:
        with open(file_path, encoding="utf-8") as config_file:
            config = json.load(config_file)
        return cls(browser, config)

    def create_page(self) -> Page:
        context = self._create_context()
        page = context.new_page()
        page.set_default_timeout(self.config.get("default_timeout_ms", self.DEFAULT_TIMEOUT_MS))
        page.set_default_navigation_timeout(
            self.config.get(
                "navigation_timeout_ms",
                self.DEFAULT_NAVIGATION_TIMEOUT_MS,
            )
        )
        return page

    def _create_context(self) -> BrowserContext:
        auth_token = self.config.get("auth_token")
        context = self.browser.new_context(
            base_url=self.config["base_url"],
            user_agent=self.config.get("user_agent", self.DEFAULT_USER_AGENT),
            viewport=self.config.get("viewport", self.DEFAULT_VIEWPORT),
            locale=self.config.get("locale", self.DEFAULT_LOCALE),
            timezone_id=self.config.get("timezone_id", self.DEFAULT_TIMEZONE_ID),
            color_scheme=self.config.get("color_scheme", self.DEFAULT_COLOR_SCHEME),
            ignore_https_errors=self.config.get(
                "ignore_https_errors",
                self.DEFAULT_IGNORE_HTTPS_ERRORS,
            ),
            extra_http_headers={
                "X-Test-Run": "true",
                "X-Source": "ui-e2e",
                **(
                    {"Authorization": f"Bearer {auth_token}"}
                    if auth_token
                    else {}
                ),
            },
        )

        if auth_token:
            context.add_cookies(
                [
                    {
                        "name": "session_token",
                        "value": auth_token,
                        "domain": "app.internal.test",
                        "path": "/",
                        "httpOnly": True,
                        "secure": True,
                    }
                ]
            )

        if self.config.get("block_analytics", self.DEFAULT_BLOCK_ANALYTICS):
            context.route("**/*", self._handle_route)

        return context
    
    def open_page(self, page: Page, page_class, path_key: str, requires_auth: bool=False):

        actions = PageActions(page)

        base_url = self.config["base_url"]
        relative_path = self.config["pages"].get(path_key, "")
        target_url = urljoin(base_url, relative_path)

        if requires_auth:
            auth = self.config["basic_auth"]
            target_url = embed_credentials_in_url(
                target_url, 
                auth["username"], 
                auth["password"]
            )

        actions.goto(target_url)

        return page_class(page, self.config)



    @staticmethod
    def _handle_route(route) -> None:
        url = route.request.url

        if "google-analytics" in url or "segment.io" in url:
            route.abort()
            return

        route.continue_()
