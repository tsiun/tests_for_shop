import pytest
from playwright.sync_api import sync_playwright
from examples.page_factory_example import PageFactory
from examples.page_object_example import LoginPage
from utils.url_utils import embed_credentials_in_url
from logger import setup_logger

@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    factory = PageFactory.from_json(browser, "config.json")
    page = factory.create_page()
    yield page
    page.close()

@pytest.fixture
def login_page(page):
    url = embed_credentials_in_url(
        "https://the-internet.herokuapp.com/basic_auth",
        username="admin",
        password="admin",
    )
    page.goto(url)
    return LoginPage(page)


# @pytest.fixture
# def login_page(page):
#     page.goto("/basic_auth")
#     return LoginPage(page)


# @pytest.fixture
# def page(page_factory):
#     #           ↓ создаёт BrowserContext + новую вкладку с нужными настройками
#     return page_factory.create_page()


# @pytest.fixture(scope="session")
# def page_factory(browser):
#     #      ↓ classmethod читает JSON и возвращает PageFactory(browser, config)
#     return PageFactory.from_json(browser, "config.json")


# @pytest.fixture
# def login_page(page, page_factory):
#     #          ↓ передаём page и config dict в BasePage
#     return LoginPage(page, page_factory.config)