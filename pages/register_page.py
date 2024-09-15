from pages.base_page import BasePage
from config.locators import RegisterPageLocators

class RegisterPage(BasePage):
    def input_email(self, email):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email_field.send_keys(email)

    def input_password(self, password):
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        password_field.send_keys(password)

    def input_confirm_password(self, password):
        password_field = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        password_field.send_keys(password)

    def click_register_button(self):
        login_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BTN)
        login_button.click()

    def assert_success_register_message(self):
        alert = self.browser.switch_to.alert
        print(alert.text)
        assert "Registered successfully!" in alert.text
        alert.accept()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()