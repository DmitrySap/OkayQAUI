from pages.base_page import BasePage
from config.locators import HomePageLocators, LoginPageLocators, RegisterPageLocators


class HomePage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(*HomePageLocators.GO_TO_LOGIN_BTN)
        login_button.click()

    def go_to_register_page(self):
        register_button = self.browser.find_element(*HomePageLocators.GO_TO_REGISTER_BTN)
        register_button.click()

    def is_login_page_loaded(self):
        title = self.browser.find_element(*LoginPageLocators.LOGIN_TITLE)
        print(f'title of login form = {title.text}')
        return title.text == "Login"

    def is_register_page_loaded(self):
        title = self.browser.find_element(*RegisterPageLocators.REGISTER_TITLE)
        print(f'title of register form = {title.text}')
        return title.text == "Register"