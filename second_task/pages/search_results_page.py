from playwright.sync_api import Page

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.filter_sort = page.get_by_test_id('filter-sort')
        self.apply_button = page.get_by_test_id('apply-filters-button')
        self.prices = page.locator('[data-testid^="search-result-price"]')
        self.loader = page.get_by_test_id('results-loader')
        self.table = page.get_by_test_id('results-content')

    def filter(self, filter_type: str):
        self.filter_sort.select_option(value=filter_type)
        self.apply_button.click()

    def wait_for_open(self):
        self.loader.wait_for(state="hidden")
        self.table.wait_for(state="visible")

    def get_elements_by_filter(self, n: int):
        prices_row = []
        for i in range(n):
            el = self.prices.nth(i)
            price = int(el.get_attribute('data-price'))
            prices_row.append(price)
        return prices_row