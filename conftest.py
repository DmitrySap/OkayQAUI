import time

import pytest
from selenium import webdriver
from config.config import Links, LoginPageData
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)  # вызвал неявное ожидание
    yield browser
    browser.quit()

@pytest.fixture()
def register(browser):
    """Регистрация"""
    link = Links.register_link
    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.input_email(LoginPageData.valid_email)
    register_page.input_password(LoginPageData.valid_password)
    register_page.input_confirm_password(LoginPageData.valid_password)
    register_page.click_register_button()
    register_page.accept_alert()

@pytest.fixture()
def login(browser, register):
    time.sleep(1)
    """Логин"""
    link = Links.login_link
    login_page = LoginPage(browser, link)
    login_page.input_email(LoginPageData.valid_email)
    login_page.input_password(LoginPageData.valid_password)
    login_page.click_login_button()