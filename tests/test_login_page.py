from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from config.config import Links, LoginPageData

class TestLogin:
    def test_login_without_filling(self, browser):
        """Попытка залогиниться, без ввода email и password"""
        link = Links.login_link
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.click_login_button()
        login_page.assert_invalid_login_message()
        assert browser.current_url != Links.dashboard_link

    def test_login_with_valid_password(self, browser, login):
        """Залогиниться с валидным email и password"""
        dashboard_page = DashboardPage(browser, self)
        dashboard_page.assert_valid_welcome()

    def test_login_with_invalid_password(self, browser, register):
        """Залогиниться с невалидным password"""
        login_page = LoginPage(browser, self)
        login_page.input_email(LoginPageData.valid_email)
        login_page.input_password(LoginPageData.invalid_password)
        login_page.click_login_button()
        login_page.assert_invalid_login_message()
        assert browser.current_url != Links.dashboard_link