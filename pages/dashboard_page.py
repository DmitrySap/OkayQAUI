from pages.base_page import BasePage
from config.locators import DashboardPageLocators


class DashboardPage(BasePage):
    def input_feedback(self, feedback):
        feedback_field = self.browser.find_element(*DashboardPageLocators.FEEDBACK_FIELD)
        feedback_field.send_keys(feedback)

    def submit_feedback(self):
        submit_button = self.browser.find_element(*DashboardPageLocators.SUBMIT_FEEDBACK_BTN)
        submit_button.click()

    def assert_feedback_too_short(self):
        alert = self.browser.switch_to.alert
        print(alert.text)
        assert "Feedback too short!" in alert.text
        alert.accept()

    def assert_feedback_submit(self):
        alert = self.browser.switch_to.alert
        print(alert.text)
        assert "Feedback submitted:" in alert.text
        alert.accept()
