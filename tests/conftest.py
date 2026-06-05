import pytest
from examples.page_factory_example import PageFactory
from examples.page_object_example import LoginPage
from utils.url_utils import embed_credentials_in_url
from utils.config_reader import ConfigReader

from logger import setup_logger

@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page_factory(browser):
    #      ↓ classmethod читает JSON и возвращает PageFactory(browser, config)
    return PageFactory.from_json(browser, "config.json")


@pytest.fixture
def page(page_factory):
    #           ↓ создаёт BrowserContext + новую вкладку с нужными настройками
    return page_factory.create_page()

@pytest.fixture
def login_page(page, page_factory):
    #          ↓ передаём page и config dict в BasePage
    return LoginPage(page, page_factory.config)