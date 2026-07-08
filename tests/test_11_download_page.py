from pages.download_page import DownloadPage
from pathlib import Path


def test_download_page(download_page: DownloadPage):
    expected_name = download_page.get_exact_file_name()

    actual_name = download_page.download_exact_file().name

    assert actual_name == expected_name, f"Expected file name: {expected_name}, but got: {actual_name}"
