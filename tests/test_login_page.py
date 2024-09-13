from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from config.config import Links, LoginPageData


def test_login_without_filling(browser):
    link = Links.login_link
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.click_login_button()
    login_page.assert_invalid_login_message()
    assert browser.current_url != Links.dashboard_link

def test_login_with_valid_password(browser):
    link = Links.register_link
    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.input_email(LoginPageData.valid_email)
    register_page.input_password(LoginPageData.valid_password)
    register_page.input_confirm_password(LoginPageData.valid_password)
    register_page.click_register_button()
    register_page.assert_success_register_message()
    assert browser.current_url == Links.login_link
    login_page = LoginPage(browser, link)
    login_page.input_email(LoginPageData.valid_email)
    login_page.input_password(LoginPageData.valid_password)
    login_page.click_login_button()
    assert browser.current_url == Links.dashboard_link

def test_login_with_invalid_password(browser):
    link = Links.register_link
    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.input_email(LoginPageData.valid_email)
    register_page.input_password(LoginPageData.valid_password)
    register_page.input_confirm_password(LoginPageData.valid_password)
    register_page.click_register_button()
    register_page.assert_success_register_message()
    assert browser.current_url == Links.login_link
    login_page = LoginPage(browser, link)
    login_page.input_email(LoginPageData.valid_email)
    login_page.input_password(LoginPageData.invalid_password)
    login_page.click_login_button()
    login_page.assert_invalid_login_message()
    assert browser.current_url != Links.dashboard_link