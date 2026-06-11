from ui.base_page import BasePage

class LoginPage(BasePage):
    _path = "/basic_auth"
    _requires_basic_auth = True
