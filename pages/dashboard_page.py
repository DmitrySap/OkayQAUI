import os
import time
from selenium.common import NoAlertPresentException
from config.config import LoginPageData
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

    def assert_valid_welcome(self):
        welcome_title = self.browser.find_element(*DashboardPageLocators.WELCOME_TITLE)
        valid_welcome = f'Welcome, {LoginPageData.valid_email}'
        assert welcome_title.text == valid_welcome, f"Ожидаемый Title:{valid_welcome}, фактический: {welcome_title.text}"

    def slider_upload_img_click(self):
        slider = self.browser.find_element(*DashboardPageLocators.SLIDER_UPLOAD_IMAGE)
        slider.click()

    def upload_img(self):
        upload_form = self.browser.find_element(*DashboardPageLocators.UPLOAD_IMG_FORM)
        if upload_form:
            print('Форма загрузки изображения появилась.')
            file_input = self.browser.find_element(*DashboardPageLocators.IMAGE_UPLOAD_BTN)
            file_path = os.path.abspath('cache/qal.png')
            file_input.send_keys(file_path)
            print('Файл успешно загружен.')
            upload_button = self.browser.find_element(*DashboardPageLocators.IMAGE_UPLOAD_SUBMIT)
            upload_button.click()
            print('Кнопка "Upload Image" нажата.')
            try:
                alert = self.browser.switch_to.alert
                valid_alert = "Success message"
                assert valid_alert in alert.text, f"Ожидаемое сообщение:'{valid_alert}', фактическое:'{alert.text}'"
                alert.accept()  # Закрываем алерт
            except NoAlertPresentException:
                raise AssertionError("Сообщение об успешной загрузке не отображается.")
