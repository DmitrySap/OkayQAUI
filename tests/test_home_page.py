from pages.home_page import HomePage
from config.config import Links


def test_home_page(browser):
    link = Links.homepage_link
    home_page = HomePage(browser, link)

    home_page.open()

    home_page.go_to_login_page()
    assert browser.current_url == Links.login_link
    assert home_page.is_login_page_loaded()

    home_page.open()

    home_page.go_to_register_page()
    assert browser.current_url == Links.register_link
    assert home_page.is_register_page_loaded()
