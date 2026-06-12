import pytest
from playwright.sync_api import sync_playwright
from examples.page_factory_example import PageFactory
from logger import setup_logger
from pages.login_page import LoginPage
from pages.login_endpoint_page import EndpointPage
from ui.page_actions import PageActions

@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session", autouse=True)
def ui_factory(browser):
    return PageFactory.from_json(browser, "config.json")


@pytest.fixture
def page(ui_factory):
    page_context = ui_factory.create_page()
    yield page_context
    page_context.close()


@pytest.fixture
def login_page(page, ui_factory):
    page_object = LoginPage(page, config = ui_factory.config)
    page_object.open('/basic_auth', requires_auth=True)
    return page_object

@pytest.fixture
def endpoint_page(page, ui_factory, login_page) -> EndpointPage:
    endpoint_page = EndpointPage(page, ui_factory.config)
    return endpoint_page
