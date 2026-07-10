from pages.upload_image_page import UploadImagePage


def test_upload_image_page(upload_image_page: UploadImagePage):
    file_path = "utils/lego_batman.jpg"
    upload_image_page.upload_file(file_path=file_path)

    actual = upload_image_page.check_result()
    expected = "lego_batman.jpg"

    assert actual == expected, f"Expected text: {expected}, but got: {actual}"
