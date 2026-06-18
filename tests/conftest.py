import pytest
from playwright.sync_api import sync_playwright
from ui.page_factory import PageFactory
from logger import setup_logger
from pages.login_page import LoginPage
from pages.login_endpoint_page import EndpointPage
from pages.alert_page import AlertPage

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
def login_page(page, ui_factory):
    return ui_factory.open_page(
        page=page,
        page_class=LoginPage,
        path_key="basic_auth",
        requires_auth=True
    )

@pytest.fixture
def endpoint_page(page, ui_factory, login_page) -> EndpointPage:
    return EndpointPage(
        page, 
        ui_factory.config
    )

@pytest.fixture
def alert_page(page, ui_factory) -> AlertPage:
    return ui_factory.open_page(
        page=page,
        page_class=AlertPage,
        path_key="javascript_alerts"
    )