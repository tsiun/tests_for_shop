from playwright.sync_api import Page
from search_results_page import SearchResultsPage

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id('search-input')
        self.submit_button = page.get_by_test_id('search-button')

    def search(self, name: str):
        self.search_input.fill(name)
        self.submit_button.click()
        search_result_page = SearchResultsPage(self.page)
        search_result_page.wait_for_open()
        return search_result_page