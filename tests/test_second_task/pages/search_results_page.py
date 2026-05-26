from playwright.sync_api import Page
from config import FILTER_TYPE

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.filter_sort = page.get_by_test_id('filter-sort')
        self.apply_button = page.get_by_test_id('apply-filters-button')
        self.all_items = page.get_by_test_id('search-results-grid').all()

    def filter(self, FILTER_TYPE: str):
        self.filter_sort.select_option(value=f"{FILTER_TYPE}")
        self.apply_button.click()

    def elements_by_filter(self, n: int):
        first_n = self.all_items[:n]
        prices = [el.text_content() for el in first_n] # я достал карточку, но как достать именно цену?



# items = page.get_by_role("listitem")

# # all() возвращает список Locator объектов
# for item in items.all():
# 		# взаимодействие происходит с каждым элементом отдельно
#     item.click()