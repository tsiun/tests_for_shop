from playwright.sync_api import Page
import pytest
from config import BASE_URL
from second_task import SearchResultsPage
from second_task import MainPage

@pytest.mark.parametrize(
    'name, n, filter_type',
    [
        pytest.param(('city', 10, 'Price: low to high'), id='city, 10, Price: low to high'),
        pytest.param(('city', 15, 'Price: high to low'), id='city, 15, Price: high to low'),
        pytest.param(('habits', 10, 'Price: low to high'), id='habits, 10, Price: low to high'),
        pytest.param(('habits', 15, 'Price: high to low'), id='habits, 15, Price: high to low')
    ]
)

def test_search_result(page: Page, name, n, filter_type):
    page.goto(BASE_URL)

    main_page = MainPage(page)
    main_page.search(name)

    search_results = SearchResultsPage(page)
    search_results.filter(filter_type)

    prices = search_results.get_elements_by_filter(n)

    assert prices == sorted(prices)