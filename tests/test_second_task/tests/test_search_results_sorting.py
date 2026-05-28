from playwright.sync_api import Page
from config import BASE_URL
from tests.test_second_task.pages.search_results_page import SearchResultsPage

def test_search_result(page: Page):
    page.goto(BASE_URL)

    search_results_page = SearchResultsPage(page)
    pass

    