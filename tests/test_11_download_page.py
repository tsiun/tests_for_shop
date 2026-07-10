from pages.download_page import DownloadPage


def test_download_page(download_page: DownloadPage):
    exact_file_position = 3
    expected_name = download_page.get_exact_file_name(
        position=exact_file_position
    )

    actual_name = download_page.download_exact_file(
        position=exact_file_position).name

    assert actual_name == expected_name, f"Expected file name: {expected_name}, but got: {actual_name}"
