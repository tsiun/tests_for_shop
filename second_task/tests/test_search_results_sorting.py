from playwright.sync_api import Page
import pytest
from second_task.pages import MainPage
from second_task.pages import SearchResultsPage
from enum import StrEnum
from second_task.utils.config_reader import ConfigReader

config = ConfigReader()
BASE_URL = config.get('BASE_URL')

class FilterType(StrEnum):
    LOW_TO_HIGH = 'Price: low to high'
    HIGH_TO_LOW = 'Price: high to low'

@pytest.mark.parametrize(
    'name, n, filter_type',
    [
        pytest.param('city', 10, FilterType.LOW_TO_HIGH),
        pytest.param('city', 15, FilterType.HIGH_TO_LOW),
        pytest.param('habits', 10, FilterType.LOW_TO_HIGH),
        pytest.param('habits', 15, FilterType.HIGH_TO_LOW)
    ]
)

def test_search_result(page: Page, name, n, filter_type):
    page.goto(BASE_URL)

    main_page = MainPage(page)
    main_page.search(name)

    search_results = SearchResultsPage(page)
    search_results.filter(filter_type)

    actual_prices = search_results.get_elements_by_filter(n)
    expected_prices = sorted(actual_prices)

    if filter_type == FilterType.HIGH_TO_LOW:
        expected_prices.reverse()

    assert actual_prices == expected_prices, \
        f"Expected prices to be sorted in {expected_prices} order, but got {actual_prices}"