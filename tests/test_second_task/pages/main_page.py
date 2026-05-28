from playwright.sync_api import Page
from config import ARTICLE_NAME
from tests.test_second_task.pages.search_results_page import SearchResultsPage


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id('search-input')
        self.submit_button = page.get_by_test_id('search-button')

    def search(self, ARTICLE_NAME: str):
        self.search_input.fill(f"{ARTICLE_NAME}")
        self.submit_button.click()
        search_result_page = SearchResultsPage(self.page)
        search_result_page.wait_for_open()
        return search_result_page