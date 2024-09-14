from selenium.common import NoAlertPresentException

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
        try:
            alert = self.browser.switch_to.alert
            valid_alert = "Feedback too short!"
            assert valid_alert in alert.text, f"Ожидаемое сообщение:'{valid_alert}', фактическое:'{alert.text}'"
            alert.accept()  # Закрываем алерт
        except NoAlertPresentException:
            raise AssertionError("Ожидаемого сообщения не было.")

    def assert_feedback_submit(self):
        try:
            alert = self.browser.switch_to.alert
            valid_alert = "Feedback submitted:"
            assert valid_alert in alert.text, f"Ожидаемое сообщение:'{valid_alert}', фактическое:'{alert.text}'"
            alert.accept()  # Закрываем алерт
        except NoAlertPresentException:
            raise AssertionError("Ожидаемого сообщения не было.")

    def click_checkboxes(self):
        checkboxes = [
            DashboardPageLocators.CHECKBOX_1,
            DashboardPageLocators.CHECKBOX_2,
            DashboardPageLocators.CHECKBOX_3
        ]
        disabled_count = 0
        for locator in checkboxes:
            checkbox = self.browser.find_element(*locator)
            if not checkbox.is_enabled():
                print(f"Чекбокс {locator[1]} отключён и не может быть выбран.")
                disabled_count += 1
                continue
            checkbox.click()
            assert checkbox.is_selected(), f"Чекбокс {locator[1]} не выбран!"
        if disabled_count > 0:
            raise AssertionError(f"Обнаружено {disabled_count} отключённых чекбоксов!")