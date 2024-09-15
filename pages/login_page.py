from pages.base_page import BasePage
from config.locators import LoginPageLocators

class LoginPage(BasePage):
    def input_email(self, email):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)

    def input_password(self, password):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.click()

    def assert_invalid_login_message(self):
        alert = self.browser.switch_to.alert
        assert "Invalid email or password!" in alert.text, 'Wrong alert text'
        alert.accept()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()