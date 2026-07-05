import pytest
from playwright.sync_api import sync_playwright
from ui.page_factory import PageFactory
from logger import setup_logger
from pages.base_auth_page import BaseAuth
from pages.alert_page import AlertPage
from pages.context_menu_page import ContextMenu
from pages.horizontal_slider_page import HorizontalSlider
from utils.url_utils import embed_credentials_in_url
from pages.hovers_page import HoversPage
from pages.windows_page import WindowsPage
from pages.nested_frames_page import NestedFrames


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
def base_auth_page(page, ui_factory) -> BaseAuth:
    ui_factory.navigate_to(page, "basic_auth", requires_auth=True)
    return BaseAuth(page, ui_factory.config)


@pytest.fixture
def alert_page(page, ui_factory) -> AlertPage:
    ui_factory.navigate_to(page, "javascript_alerts")
    return AlertPage(page, ui_factory.config)


@pytest.fixture
def context_menu_page(page, ui_factory) -> ContextMenu:
    ui_factory.navigate_to(page, "context_menu")
    return ContextMenu(page, ui_factory.config)


@pytest.fixture
def horizontal_slider_page(page, ui_factory) -> HorizontalSlider:
    ui_factory.navigate_to(page, "horizontal_slider")
    return HorizontalSlider(page, ui_factory.config)


@pytest.fixture
def hovers_page(page, ui_factory) -> HoversPage:
    ui_factory.navigate_to(page, "hovers")
    return HoversPage(page, ui_factory.config)


@pytest.fixture
def windows_page(page, ui_factory) -> WindowsPage:
    ui_factory.navigate_to(page, "windows")
    return WindowsPage(page, ui_factory.config)


@pytest.fixture
def nested_frames_page(page, ui_factory) -> NestedFrames:
    ui_factory.navigate_to(page, "nested_frames")
    return NestedFrames(page, ui_factory.config)
