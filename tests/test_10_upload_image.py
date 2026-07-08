from pages.upload_image_page import UploadImagePage


def test_upload_image_page(upload_image_page: UploadImagePage):
    upload_image_page.upload_file()

    actual = upload_image_page.check_result()
    expected = "lego_batman.jpg"

    assert actual == expected, f"Expected text: {expected}, but got: {actual}"
