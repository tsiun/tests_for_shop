import pytest
from playwright.sync_api import sync_playwright
from ui.page_factory import PageFactory
from logger import setup_logger
from pages.base_auth_page import BaseAuthPage
from pages.alert_page import AlertPage
from pages.context_menu_page import ContextMenuPage
from pages.horizontal_slider_page import HorizontalSliderPage
from utils.url_utils import embed_credentials_in_url
from pages.hovers_page import HoversPage
from pages.windows_page import WindowsPage
from pages.nested_frames_page import NestedFramesPage
from pages.dynamic_content_page import DynamicContentPage


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="session")
def browser():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    yield browser
    browser.close()
    pw.stop()


@pytest.fixture(scope="session")
def ui_factory(browser):
    return PageFactory.from_json(browser, "config.json")


@pytest.fixture
def page(ui_factory):
    page_obj = ui_factory.create_page()
    yield page_obj
    page_obj.context.close()


@pytest.fixture
def base_auth_page(page, ui_factory) -> BaseAuthPage:
    ui_factory.navigate_to(page, "basic_auth", requires_auth=True)
    return BaseAuthPage(page, ui_factory.config)


@pytest.fixture
def alert_page(page, ui_factory) -> AlertPage:
    ui_factory.navigate_to(page, "javascript_alerts")
    return AlertPage(page, ui_factory.config)


@pytest.fixture
def context_menu_page(page, ui_factory) -> ContextMenuPage:
    ui_factory.navigate_to(page, "context_menu")
    return ContextMenuPage(page, ui_factory.config)


@pytest.fixture
def horizontal_slider_page(page, ui_factory) -> HorizontalSliderPage:
    ui_factory.navigate_to(page, "horizontal_slider")
    return HorizontalSliderPage(page, ui_factory.config)


@pytest.fixture
def hovers_page(page, ui_factory) -> HoversPage:
    ui_factory.navigate_to(page, "hovers")
    return HoversPage(page, ui_factory.config)


@pytest.fixture
def windows_page(page, ui_factory) -> WindowsPage:
    ui_factory.navigate_to(page, "windows")
    return WindowsPage(page, ui_factory.config)


@pytest.fixture
def nested_frames_page(page, ui_factory) -> NestedFramesPage:
    ui_factory.navigate_to(page, "nested_frames")
    return NestedFramesPage(page, ui_factory.config)


@pytest.fixture
def dynamic_content_page(page, ui_factory) -> DynamicContentPage:
    ui_factory.navigate_to(page, "/dynamic_content")
    return DynamicContentPage(page, ui_factory.config)
